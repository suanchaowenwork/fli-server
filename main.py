from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from typing import Optional, List
from pydantic import BaseModel

from fli.models import (
    Airport, PassengerInfo, SeatType, MaxStops, SortBy,
    FlightSearchFilters, FlightSegment, DateSearchFilters
)
from fli.search import SearchFlights, SearchDates
from airports import search_airports

app = FastAPI(title="Fli API", description="API de vuelos con Google Flights")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchFlightsRequest(BaseModel):
    origin: str
    destination: str
    departure_date: str
    return_date: Optional[str] = None
    adults: int = 1
    children: int = 0
    seniors: int = 0
    cabin_class: str = "ECONOMY"
    max_stops: str = "ANY"
    sort_by: str = "CHEAPEST"

@app.get("/health")
def health():
    return {"status": "ok", "service": "fli-server", "timestamp": datetime.now().isoformat()}

@app.get("/airports/search")
def get_airports(q: str = Query(..., min_length=1), limit: int = Query(10, ge=1, le=20)):
    """Busca aeropuertos por nombre, ciudad o código IATA"""
    results = search_airports(q, limit)
    return {"airports": results, "count": len(results), "query": q}

@app.get("/airports/popular")
def get_popular_airports():
    """Devuelve los aeropuertos más populares"""
    from airports import AIRPORTS
    popular = [a for a in AIRPORTS if a["iata"] in ["BOG", "MDE", "CTG", "MIA", "MCO", "JFK", "CUN", "MEX", "MAD", "CDG", "LHR", "BCN"]]
    return {"airports": popular}

@app.post("/search-flights")
def search_flights(req: SearchFlightsRequest):
    try:
        seat_type = getattr(SeatType, req.cabin_class, SeatType.ECONOMY)
        max_stops = getattr(MaxStops, req.max_stops, MaxStops.ANY)
        sort_by = getattr(SortBy, req.sort_by, SortBy.CHEAPEST)

        passenger_info = PassengerInfo(
            adults=req.adults,
            children=req.children if req.children > 0 else None,
            seniors=req.seniors if req.seniors > 0 else None,
        )

        origin_airport = getattr(Airport, req.origin, None)
        dest_airport = getattr(Airport, req.destination, None)
        
        if not origin_airport:
            raise HTTPException(status_code=400, detail=f"Aeropuerto origen '{req.origin}' no encontrado. Usa /airports/search para buscar.")
        if not dest_airport:
            raise HTTPException(status_code=400, detail=f"Aeropuerto destino '{req.destination}' no encontrado. Usa /airports/search para buscar.")

        segments = [
            FlightSegment(
                departure_airport=[[origin_airport, 0]],
                arrival_airport=[[dest_airport, 0]],
                travel_date=req.departure_date,
            )
        ]

        if req.return_date:
            segments.append(
                FlightSegment(
                    departure_airport=[[dest_airport, 0]],
                    arrival_airport=[[origin_airport, 0]],
                    travel_date=req.return_date,
                )
            )

        filters = FlightSearchFilters(
            passenger_info=passenger_info,
            flight_segments=segments,
            seat_type=seat_type,
            stops=max_stops,
            sort_by=sort_by,
        )

        search = SearchFlights()
        results = search.search(filters)

        flights = []
        for flight in results[:20]:
            legs = []
            for leg in flight.legs:
                legs.append({
                    "airline": leg.airline.value if hasattr(leg.airline, 'value') else str(leg.airline),
                    "flight_number": leg.flight_number,
                    "departure_airport": leg.departure_airport.value if hasattr(leg.departure_airport, 'value') else str(leg.departure_airport),
                    "arrival_airport": leg.arrival_airport.value if hasattr(leg.arrival_airport, 'value') else str(leg.arrival_airport),
                    "departure_datetime": leg.departure_datetime.isoformat() if leg.departure_datetime else None,
                    "arrival_datetime": leg.arrival_datetime.isoformat() if leg.arrival_datetime else None,
                })

            flights.append({
                "price": flight.price,
                "currency": flight.currency if hasattr(flight, 'currency') else "COP",
                "duration": flight.duration,
                "stops": flight.stops,
                "legs": legs,
            })

        return {"flights": flights, "count": len(flights)}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search-dates")
def search_dates(
    origin: str,
    destination: str,
    start_date: str,
    end_date: str,
    trip_duration: Optional[int] = 7,
    is_round_trip: bool = True,
    adults: int = 1,
    cabin_class: str = "ECONOMY",
):
    try:
        seat_type = getattr(SeatType, cabin_class, SeatType.ECONOMY)
        passenger_info = PassengerInfo(adults=adults)
        
        origin_airport = getattr(Airport, origin, None)
        dest_airport = getattr(Airport, destination, None)
        
        if not origin_airport or not dest_airport:
            raise HTTPException(status_code=400, detail="Aeropuerto no encontrado")

        filters = DateSearchFilters(
            passenger_info=passenger_info,
            departure_airport=origin_airport,
            arrival_airport=dest_airport,
            start_date=start_date,
            end_date=end_date,
            trip_duration=trip_duration,
            is_round_trip=is_round_trip,
            seat_type=seat_type,
        )

        search = SearchDates()
        results = search.search(filters)

        dates = []
        for result in results[:30]:
            dates.append({
                "departure_date": result.departure_date.isoformat() if result.departure_date else None,
                "return_date": result.return_date.isoformat() if result.return_date else None,
                "price": result.price,
                "currency": result.currency if hasattr(result, 'currency') else "COP",
            })

        return {"dates": dates, "count": len(dates)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
