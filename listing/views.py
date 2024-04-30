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
    NUM_PEL = len(Listing.nodes.all())
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
    
    listing = Listing.nodes.all()[(pag-1)*TAM_PAG:pag*TAM_PAG]
    return render(request, 'list/listListing.html', {
        'total': NUM_PEL,
        'listing': listing,
        'pagina':pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL':settings.STATIC_URL
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
