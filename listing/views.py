from django.http import JsonResponse
from django.shortcuts import render
from neomodel import Traversal, match, db

from .models import Amenity, Neighborhood, Host, User, Review, Listing
from django.conf import settings


def index(request):
    return render(request, 'index.html', {
        'STATIC_URL':settings.STATIC_URL
    })

def listListing(request, pag):
    TAM_PAG = 10
    
    # Realiza una consulta para contar el total de Listings
    count_query = "MATCH (n:Listing) RETURN count(n)"
    count_results, _ = db.cypher_query(count_query)
    NUM_PEL = count_results[0][0] if count_results else 0
    NUM_PAG = (NUM_PEL + TAM_PAG - 1) // TAM_PAG  # Calcula el número total de páginas

    # Asegúrate de que la página solicitada esté dentro de los límites
    pag = max(1, min(pag, NUM_PAG))
    
    # Calcula el rango de páginas para la paginación
    start_page = max(1, pag - 3)
    end_page = min(NUM_PAG, pag + 3)
    paginas = range(start_page, end_page + 1)

    # Calcula el offset para la consulta
    offset = (pag - 1) * TAM_PAG
    
    # Realiza una consulta para obtener los Listings de la página actual
    query = """
    MATCH (n:Listing)
    RETURN n
    SKIP $offset
    LIMIT $limit
    """
    listing_results, _ = db.cypher_query(query, {'offset': offset, 'limit': TAM_PAG})
    listings = [Listing.inflate(row[0]) for row in listing_results]

    return render(request, 'list/listListing.html', {
        'total': NUM_PEL,
        'listing': listings,
        'pagina': pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL': settings.STATIC_URL
    })


def listHost(request, pag):
    NUM_PEL = len(Host.nodes.all())
    TAM_PAG = 10
    NUM_PAG = int(NUM_PEL/TAM_PAG)
    if pag > NUM_PAG:
        pag = NUM_PAG
    else:
        if pag < 1:
            pag = 1
    if pag - 3 < 1:
        paginas = range(1,pag + 4)
    elif pag+3 > NUM_PAG:
        paginas = range(pag - 3, NUM_PAG+1)
    else:
        paginas = range(pag - 3,pag + 4)
    
    host = Host.nodes.all()[(pag-1)*TAM_PAG:pag*TAM_PAG]
    return render(request, 'list/listHost.html', {
        'total': NUM_PEL,
        'host': host,
        'pagina':pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL':settings.STATIC_URL
    })

def listNeighborhood(request, pag):
    NUM_PEL = len(Neighborhood.nodes.all())
    TAM_PAG = 10
    NUM_PAG = int(NUM_PEL/TAM_PAG)
    if pag > NUM_PAG:
        pag = NUM_PAG
    else:
        if pag < 1:
            pag = 1
    if pag - 3 < 1:
        paginas = range(1,pag + 4)
    elif pag+3 > NUM_PAG:
        paginas = range(pag - 3, NUM_PAG+1)
    else:
        paginas = range(pag - 3,pag + 4)
    
    neighborhood = Neighborhood.nodes.all()[(pag-1)*TAM_PAG:pag*TAM_PAG]
    return render(request, 'list/listNeighborhood.html', {
        'total': NUM_PEL,
        'neighborhood': neighborhood,
        'pagina':pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL':settings.STATIC_URL
    })

def listAmenity(request, pag):
    NUM_PEL = len(Amenity.nodes.all())
    TAM_PAG = 10
    NUM_PAG = int(NUM_PEL/TAM_PAG)
    if pag > NUM_PAG:
        pag = NUM_PAG
    else:
        if pag < 1:
            pag = 1
    if pag - 3 < 1:
        paginas = range(1,pag + 4)
    elif pag+3 > NUM_PAG:
        paginas = range(pag - 3, NUM_PAG+1)
    else:
        paginas = range(pag - 3,pag + 4)
    
    amenity = Amenity.nodes.all()[(pag-1)*TAM_PAG:pag*TAM_PAG]
    return render(request, 'list/listAmenity.html', {
        'total': NUM_PEL,
        'amenity': amenity,
        'pagina':pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL':settings.STATIC_URL
    })

def listUser(request, pag):
    NUM_PEL = len(User.nodes.all())
    TAM_PAG = 10
    NUM_PAG = int(NUM_PEL/TAM_PAG)
    if pag > NUM_PAG:
        pag = NUM_PAG
    else:
        if pag < 1:
            pag = 1
    if pag - 3 < 1:
        paginas = range(1,pag + 4)
    elif pag+3 > NUM_PAG:
        paginas = range(pag - 3, NUM_PAG+1)
    else:
        paginas = range(pag - 3,pag + 4)
    
    user = User.nodes.all()[(pag-1)*TAM_PAG:pag*TAM_PAG]
    return render(request, 'list/listUser.html', {
        'total': NUM_PEL,
        'user': user,
        'pagina':pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL':settings.STATIC_URL
    })

def listReview(request, pag):
    NUM_PEL = len(Review.nodes.all())
    TAM_PAG = 10
    NUM_PAG = int(NUM_PEL/TAM_PAG)
    if pag > NUM_PAG:
        pag = NUM_PAG
    else:
        if pag < 1:
            pag = 1
    if pag - 3 < 1:
        paginas = range(1,pag + 4)
    elif pag+3 > NUM_PAG:
        paginas = range(pag - 3, NUM_PAG+1)
    else:
        paginas = range(pag - 3,pag + 4)
    
    review = Review.nodes.all()[(pag-1)*TAM_PAG:pag*TAM_PAG]
    return render(request, 'list/listReview.html', {
        'total': NUM_PEL,
        'review': review,
        'pagina':pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL':settings.STATIC_URL
    })

def getListing(request, id):
    listing = Listing.nodes.get(listing_id = id)
    reviews = listing.reviews.all()
    host = listing.host.all()
    amenities = listing.amenities.all()
    neighborhood = listing.neighborhood.all()[0]
    return render(request, 'details/detailsListing.html', {
        'neighborhood': neighborhood,
        'amenities': amenities,
        'host': host,
        'review': reviews,
        'listing': listing,
        'STATIC_URL':settings.STATIC_URL
    })

def getHost(request, id):
    host = Host.nodes.get(host_id = id)
    listing = host.listings.all()
    
    return render(request, 'details/detailsHost.html', {
        'host': host,
        'listing': listing,
        'STATIC_URL':settings.STATIC_URL
    })

def getNeighborhood(request, id):
    neighborhood = Neighborhood.nodes.get(neighborhood_id = id)
    listing = neighborhood.listings.all()
    
    return render(request, 'details/detailsNeighborhood.html', {
        'neighborhood': neighborhood,
        'listing': listing,
        'STATIC_URL':settings.STATIC_URL
    })

def getAmenity(request, id):
    amenities = Amenity.nodes.get(name = id)
    listing = amenities.listings.all()
    
    return render(request, 'details/detailsAmenity.html', {
        'amenities': amenities,
        'listing': listing,
        'STATIC_URL':settings.STATIC_URL
    })

def getUser(request, id):
    user = User.nodes.get(user_id = id)
    review = user.reviews.all()
   
    return render(request, 'details/detailsUser.html', {
        'user': user,
        'review': review,
        'STATIC_URL':settings.STATIC_URL
    })

def getReview(request, id):
    reviews = Review.nodes.get(review_id = id)
    listing = reviews.listings.all()
    user = reviews.user.all()

    return render(request, 'details/detailsReview.html', {
        'user': user,
        'review': reviews,
        'listing': listing,
        'STATIC_URL':settings.STATIC_URL
    })

def getMostRatedListing(request):
    # Realizamos una consulta Cypher para encontrar el Listing con más Reviews
    query = """
    MATCH (review)-[r:REVIEWS]->(l:Listing)
    RETURN l, COUNT(review) as reviews_count
    ORDER BY reviews_count DESC
    LIMIT 1
    """
    results, meta = db.cypher_query(query)

    # Verificamos si hay resultados
    if results:
        most_rated_listing, reviews_count = results[0][0], results[0][1]
        
        # Convertimos el nodo Neo4j en un objeto Django Neomodel para acceder fácilmente a sus relaciones
        most_rated_listing = Listing.inflate(most_rated_listing)
        
        # Preparamos los detalles para renderizar la respuesta
        reviews = most_rated_listing.reviews.all()
        host = most_rated_listing.host.all()
        amenities = most_rated_listing.amenities.all()
        neighborhood = most_rated_listing.neighborhood.all()[0]  # Asumiendo que cada listing está en un vecindario

        return render(request, 'details/detailsListing.html', {
            'neighborhood': neighborhood,
            'amenities': amenities,
            'host': host,
            'review': reviews,
            'listing': most_rated_listing,
            'STATIC_URL':settings.STATIC_URL
        })
    else:
        # Si no hay resultados, devolvemos un error
        return JsonResponse({'error': 'No listings with reviews found'}, status=404)