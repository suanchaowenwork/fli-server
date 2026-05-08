AIRPORTS = [
    {"iata": "BOG", "name": "El Dorado Intl", "city": "Bogotá", "country": "Colombia"},
    {"iata": "MDE", "name": "José María Córdova", "city": "Medellín", "country": "Colombia"},
    {"iata": "CTG", "name": "Rafael Núñez", "city": "Cartagena", "country": "Colombia"},
    {"iata": "CLO", "name": "Alfonso Bonilla Aragón", "city": "Cali", "country": "Colombia"},
    {"iata": "BAQ", "name": "Ernesto Cortissoz", "city": "Barranquilla", "country": "Colombia"},
    {"iata": "SMR", "name": "Simón Bolívar", "city": "Santa Marta", "country": "Colombia"},
    {"iata": "PEI", "name": "Matecaña", "city": "Pereira", "country": "Colombia"},
    {"iata": "BGA", "name": "Palonegro", "city": "Bucaramanga", "country": "Colombia"},
    {"iata": "CUC", "name": "Camilo Daza", "city": "Cúcuta", "country": "Colombia"},
    {"iata": "ADZ", "name": "Gustavo Rojas Pinilla", "city": "San Andrés", "country": "Colombia"},
    {"iata": "MIA", "name": "Miami Intl", "city": "Miami", "country": "USA"},
    {"iata": "MCO", "name": "Orlando Intl", "city": "Orlando", "country": "USA"},
    {"iata": "JFK", "name": "John F. Kennedy", "city": "New York", "country": "USA"},
    {"iata": "LAX", "name": "Los Angeles Intl", "city": "Los Angeles", "country": "USA"},
    {"iata": "FLL", "name": "Fort Lauderdale", "city": "Fort Lauderdale", "country": "USA"},
    {"iata": "ATL", "name": "Hartsfield-Jackson", "city": "Atlanta", "country": "USA"},
    {"iata": "DFW", "name": "Dallas/Fort Worth", "city": "Dallas", "country": "USA"},
    {"iata": "IAH", "name": "George Bush", "city": "Houston", "country": "USA"},
    {"iata": "SFO", "name": "San Francisco Intl", "city": "San Francisco", "country": "USA"},
    {"iata": "ORD", "name": "O'Hare Intl", "city": "Chicago", "country": "USA"},
    {"iata": "LAS", "name": "Harry Reid Intl", "city": "Las Vegas", "country": "USA"},
    {"iata": "PHX", "name": "Sky Harbor", "city": "Phoenix", "country": "USA"},
    {"iata": "DEN", "name": "Denver Intl", "city": "Denver", "country": "USA"},
    {"iata": "SEA", "name": "Seattle-Tacoma", "city": "Seattle", "country": "USA"},
    {"iata": "BOS", "name": "Logan Intl", "city": "Boston", "country": "USA"},
    {"iata": "CUN", "name": "Cancún Intl", "city": "Cancún", "country": "México"},
    {"iata": "MEX", "name": "Benito Juárez", "city": "Ciudad de México", "country": "México"},
    {"iata": "GDL", "name": "Miguel Hidalgo", "city": "Guadalajara", "country": "México"},
    {"iata": "PUJ", "name": "Punta Cana Intl", "city": "Punta Cana", "country": "República Dominicana"},
    {"iata": "SDQ", "name": "Las Américas", "city": "Santo Domingo", "country": "República Dominicana"},
    {"iata": "HAV", "name": "José Martí", "city": "La Habana", "country": "Cuba"},
    {"iata": "SJO", "name": "Juan Santamaría", "city": "San José", "country": "Costa Rica"},
    {"iata": "PTY", "name": "Tocumen Intl", "city": "Panamá", "country": "Panamá"},
    {"iata": "LIM", "name": "Jorge Chávez", "city": "Lima", "country": "Perú"},
    {"iata": "SCL", "name": "Arturo Merino Benítez", "city": "Santiago", "country": "Chile"},
    {"iata": "EZE", "name": "Ministro Pistarini", "city": "Buenos Aires", "country": "Argentina"},
    {"iata": "GRU", "name": "Guarulhos", "city": "São Paulo", "country": "Brasil"},
    {"iata": "GIG", "name": "Galeão", "city": "Río de Janeiro", "country": "Brasil"},
    {"iata": "MAD", "name": "Adolfo Suárez", "city": "Madrid", "country": "España"},
    {"iata": "BCN", "name": "Josep Tarradellas", "city": "Barcelona", "country": "España"},
    {"iata": "CDG", "name": "Charles de Gaulle", "city": "París", "country": "Francia"},
    {"iata": "LHR", "name": "Heathrow", "city": "Londres", "country": "Reino Unido"},
    {"iata": "FCO", "name": "Leonardo da Vinci", "city": "Roma", "country": "Italia"},
    {"iata": "AMS", "name": "Schiphol", "city": "Ámsterdam", "country": "Países Bajos"},
    {"iata": "FRA", "name": "Frankfurt", "city": "Frankfurt", "country": "Alemania"},
    {"iata": "IST", "name": "Istanbul", "city": "Estambul", "country": "Turquía"},
    {"iata": "DXB", "name": "Dubai Intl", "city": "Dubai", "country": "Emiratos Árabes"},
    {"iata": "DOH", "name": "Hamad Intl", "city": "Doha", "country": "Qatar"},
    {"iata": "SIN", "name": "Changi", "city": "Singapur", "country": "Singapur"},
    {"iata": "HND", "name": "Haneda", "city": "Tokio", "country": "Japón"},
    {"iata": "ICN", "name": "Incheon", "city": "Seúl", "country": "Corea del Sur"},
    {"iata": "BKK", "name": "Suvarnabhumi", "city": "Bangkok", "country": "Tailandia"},
    {"iata": "SYD", "name": "Kingsford Smith", "city": "Sídney", "country": "Australia"},
    {"iata": "AKL", "name": "Auckland", "city": "Auckland", "country": "Nueva Zelanda"},
    {"iata": "JNB", "name": "O.R. Tambo", "city": "Johannesburgo", "country": "Sudáfrica"},
    {"iata": "CAI", "name": "Cairo Intl", "city": "El Cairo", "country": "Egipto"},
    {"iata": "CMN", "name": "Mohammed V", "city": "Casablanca", "country": "Marruecos"},
]

def search_airports(query: str, limit: int = 10):
    """Busca aeropuertos por ciudad, nombre o código IATA"""
    query = query.lower().strip()
    if not query:
        return []
    
    results = []
    for airport in AIRPORTS:
        score = 0
        # Coincidencia exacta de IATA (máxima prioridad)
        if airport["iata"].lower() == query:
            score = 100
        # Coincidencia parcial de IATA
        elif query in airport["iata"].lower():
            score = 80
        # Coincidencia exacta de ciudad
        elif airport["city"].lower() == query:
            score = 70
        # Coincidencia parcial de ciudad
        elif query in airport["city"].lower():
            score = 60
        # Coincidencia parcial de nombre
        elif query in airport["name"].lower():
            score = 50
        # Coincidencia parcial de país
        elif query in airport["country"].lower():
            score = 30
        
        if score > 0:
            results.append({**airport, "score": score})
    
    # Ordenar por score descendente
    results.sort(key=lambda x: x["score"], reverse=True)
    
    # Eliminar el campo score del resultado
    for r in results:
        del r["score"]
    
    return results[:limit]
