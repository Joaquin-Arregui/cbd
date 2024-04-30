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
    TAM_PAG = 10

    count_query = "MATCH (n:Host) RETURN count(n)"
    count_results, _ = db.cypher_query(count_query)
    NUM_PEL = count_results[0][0] if count_results else 0
    NUM_PAG = (NUM_PEL + TAM_PAG - 1) // TAM_PAG  

    pag = max(1, min(pag, NUM_PAG))
    
    start_page = max(1, pag - 3)
    end_page = min(NUM_PAG, pag + 3)
    paginas = range(start_page, end_page + 1)

    offset = (pag - 1) * TAM_PAG
    
    query = """
    MATCH (n:Host)
    RETURN n
    SKIP $offset
    LIMIT $limit
    """
    params = {'offset': offset, 'limit': TAM_PAG}
    host_results, _ = db.cypher_query(query, params)
    hosts = [Host.inflate(row[0]) for row in host_results]

    return render(request, 'list/listHost.html', {
        'total': NUM_PEL,
        'host': hosts,
        'pagina': pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL': settings.STATIC_URL
    })

def listNeighborhood(request, pag):
    TAM_PAG = 10

    count_query = "MATCH (n:Neighborhood) RETURN count(n)"
    count_results, _ = db.cypher_query(count_query)
    NUM_PEL = count_results[0][0] if count_results else 0
    NUM_PAG = (NUM_PEL + TAM_PAG - 1) // TAM_PAG  

    pag = max(1, min(pag, NUM_PAG))
    
    start_page = max(1, pag - 3)
    end_page = min(NUM_PAG, pag + 3)
    paginas = range(start_page, end_page + 1)

    offset = (pag - 1) * TAM_PAG
    
    query = """
    MATCH (n:Neighborhood)
    RETURN n
    SKIP $offset
    LIMIT $limit
    """
    params = {'offset': offset, 'limit': TAM_PAG}
    neighborhood_results, _ = db.cypher_query(query, params)
    neighborhoods = [Neighborhood.inflate(row[0]) for row in neighborhood_results]

    return render(request, 'list/listNeighborhood.html', {
        'total': NUM_PEL,
        'neighborhood': neighborhoods,
        'pagina': pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL': settings.STATIC_URL
    })

def listAmenity(request, pag):
    TAM_PAG = 10

    count_query = "MATCH (a:Amenity) RETURN count(a)"
    count_results, _ = db.cypher_query(count_query)
    NUM_PEL = count_results[0][0] if count_results else 0
    NUM_PAG = (NUM_PEL + TAM_PAG - 1) // TAM_PAG  

    pag = max(1, min(pag, NUM_PAG))
    
    start_page = max(1, pag - 3)
    end_page = min(NUM_PAG, pag + 3)
    paginas = range(start_page, end_page + 1)

    offset = (pag - 1) * TAM_PAG
    
    query = """
    MATCH (a:Amenity)
    RETURN a
    SKIP $offset
    LIMIT $limit
    """
    params = {'offset': offset, 'limit': TAM_PAG}
    amenity_results, _ = db.cypher_query(query, params)
    amenities = [Amenity.inflate(row[0]) for row in amenity_results]

    return render(request, 'list/listAmenity.html', {
        'total': NUM_PEL,
        'amenity': amenities,
        'pagina': pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL': settings.STATIC_URL
    })

def listUser(request, pag):
    TAM_PAG = 10

    count_query = "MATCH (u:User) RETURN count(u)"
    count_results, _ = db.cypher_query(count_query)
    NUM_PEL = count_results[0][0] if count_results else 0
    NUM_PAG = (NUM_PEL + TAM_PAG - 1) // TAM_PAG  

    pag = max(1, min(pag, NUM_PAG))

    start_page = max(1, pag - 3)
    end_page = min(NUM_PAG, pag + 3)
    paginas = range(start_page, end_page + 1)

    offset = (pag - 1) * TAM_PAG

    query = """
    MATCH (u:User)
    RETURN u
    SKIP $offset
    LIMIT $limit
    """
    params = {'offset': offset, 'limit': TAM_PAG}
    user_results, _ = db.cypher_query(query, params)
    users = [User.inflate(row[0]) for row in user_results]

    return render(request, 'list/listUser.html', {
        'total': NUM_PEL,
        'user': users,
        'pagina': pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL': settings.STATIC_URL
    })

def listReview(request, pag):
    TAM_PAG = 10

    count_query = "MATCH (r:Review) RETURN count(r)"
    count_results, _ = db.cypher_query(count_query)
    NUM_PEL = count_results[0][0] if count_results else 0
    NUM_PAG = (NUM_PEL + TAM_PAG - 1) // TAM_PAG  

    pag = max(1, min(pag, NUM_PAG))

    start_page = max(1, pag - 3)
    end_page = min(NUM_PAG, pag + 3)
    paginas = range(start_page, end_page + 1)

    offset = (pag - 1) * TAM_PAG

    query = """
    MATCH (r:Review)
    RETURN r
    SKIP $offset
    LIMIT $limit
    """
    params = {'offset': offset, 'limit': TAM_PAG}
    review_results, _ = db.cypher_query(query, params)
    reviews = [Review.inflate(row[0]) for row in review_results]

    return render(request, 'list/listReview.html', {
        'total': NUM_PEL,
        'review': reviews,
        'pagina': pag,
        'paginas': paginas,
        'total_paginas': NUM_PAG,
        'STATIC_URL': settings.STATIC_URL
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