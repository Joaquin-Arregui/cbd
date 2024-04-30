from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from neomodel import Traversal, match, db

from .models import Amenity, Neighborhood, Host, User, Review, Listing
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Review, Listing
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {
        'STATIC_URL':settings.STATIC_URL
    })

def listListing(request, pag):
    TAM_PAG = 10
    
    count_query = "MATCH (n:Listing) RETURN count(n)"
    count_results, _ = db.cypher_query(count_query)
    NUM_PEL = count_results[0][0] if count_results else 0
    NUM_PAG = (NUM_PEL + TAM_PAG - 1) // TAM_PAG  

    pag = max(1, min(pag, NUM_PAG))
    
    start_page = max(1, pag - 3)
    end_page = min(NUM_PAG, pag + 3)
    paginas = range(start_page, end_page + 1)

    offset = (pag - 1) * TAM_PAG
    
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
    query = """
    MATCH (l:Listing)
    WHERE l.listing_id = $id
    RETURN l
    """
    results, _ = db.cypher_query(query, {'id': str(id)})
    
    if results:
        listing = results[0][0]
        listing = Listing.inflate(listing)
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
            'STATIC_URL': settings.STATIC_URL
        })
    else:
        return render(request, 'details/detailsListing.html', {
            'error': 'No listing found with the provided ID.',
            'STATIC_URL': settings.STATIC_URL
        })

def getHost(request, id):
    query = """
    MATCH (h:Host)
    WHERE h.host_id = $id
    RETURN h
    """
    results, _ = db.cypher_query(query, {'id': str(id)})
    
    if results:
        host = results[0][0]
        host = Host.inflate(host)
        listings = host.listings.all()

        return render(request, 'details/detailsHost.html', {
            'host': host,
            'listing': listings,
            'STATIC_URL': settings.STATIC_URL
        })
    else:
        return render(request, 'details/detailsHost.html', {
            'error': 'No host found with the provided ID.',
            'STATIC_URL': settings.STATIC_URL
        })


def getNeighborhood(request, id):
    query = """
    MATCH (n:Neighborhood)
    WHERE n.neighborhood_id = $id
    RETURN n
    """
    results, _ = db.cypher_query(query, {'id': str(id)})
    
    if results:
        neighborhood = results[0][0]
        neighborhood = Neighborhood.inflate(neighborhood)
        listings = neighborhood.listings.all()

        return render(request, 'details/detailsNeighborhood.html', {
            'neighborhood': neighborhood,
            'listing': listings,
            'STATIC_URL': settings.STATIC_URL
        })
    else:
        return render(request, 'details/detailsNeighborhood.html', {
            'error': 'No neighborhood found with the provided ID.',
            'STATIC_URL': settings.STATIC_URL
        })


def getAmenity(request, id):
    query = """
    MATCH (a:Amenity)
    WHERE a.name = $id
    RETURN a
    """
    results, _ = db.cypher_query(query, {'id': str(id)})
    
    if results:
        amenity = results[0][0]
        amenity = Amenity.inflate(amenity)
        listings = amenity.listings.all()

        return render(request, 'details/detailsAmenity.html', {
            'amenities': amenity,
            'listing': listings,
            'STATIC_URL': settings.STATIC_URL
        })
    else:
        return render(request, 'details/detailsAmenity.html', {
            'error': 'No amenity found with the provided ID.',
            'STATIC_URL': settings.STATIC_URL
        })

def getUser(request, id):
    query = """
    MATCH (u:User {user_id: $id})
    RETURN u
    """
    results, _ = db.cypher_query(query, {'id': str(id)})
    
    if results:
        user = results[0][0]
        user = User.inflate(user)
        reviews = user.reviews.all()

        return render(request, 'details/detailsUser.html', {
            'user': user,
            'review': reviews,
            'STATIC_URL': settings.STATIC_URL
        })
    else:
        return render(request, 'details/detailsUser.html', {
            'error': 'No user found with the provided ID.',
            'STATIC_URL': settings.STATIC_URL
        })

def getReview(request, id):
    query = """
    MATCH (r:Review)
    WHERE r.review_id = $id
    RETURN r
    """
    results, _ = db.cypher_query(query, {'id': str(id)})
    
    if results:
        reviews = results[0][0]
        reviews = Review.inflate(reviews)
        listing = reviews.listings.all()
        user = reviews.user.all()
        return render(request, 'details/detailsReview.html', {
            'user': user,
            'review': reviews,
            'listing': listing,
            'STATIC_URL': settings.STATIC_URL
        })
    else:
        return render(request, 'details/detailsReview.html', {
            'error': 'No review found with the provided ID.',
            'STATIC_URL': settings.STATIC_URL
        })

def getMostRatedListing(request):
    query = """
    MATCH (review)-[r:REVIEWS]->(l:Listing)
    RETURN l, COUNT(review) as reviews_count
    ORDER BY reviews_count DESC
    LIMIT 1
    """
    results, meta = db.cypher_query(query)

    if results:
        most_rated_listing, reviews_count = results[0][0], results[0][1]
        
        most_rated_listing = Listing.inflate(most_rated_listing)

        reviews = most_rated_listing.reviews.all()
        host = most_rated_listing.host.all()
        amenities = most_rated_listing.amenities.all()
        neighborhood = most_rated_listing.neighborhood.all()[0]  

        return render(request, 'details/detailsListing.html', {
            'neighborhood': neighborhood,
            'amenities': amenities,
            'host': host,
            'review': reviews,
            'listing': most_rated_listing,
            'STATIC_URL':settings.STATIC_URL
        })
    else:
        return JsonResponse({'error': 'No listings with reviews found'}, status=404)

def create_review(request, listing_id):
    query = """
    MATCH (u:Listing {listing_id: $id})
    RETURN u
    """
    results, _ = db.cypher_query(query, {'id': str(listing_id)})
    listing = results[0][0]
    listing = Listing.inflate(listing)
    if not listing:
        return JsonResponse({'error': 'Listing not found'}, status=404)
    
    if request.method == 'POST':
        review_text = request.POST.get('comment')
        id = request.POST.get('user')
        query = """
        MATCH (u:User {user_id: $id})
        RETURN u
        """
        results, _ = db.cypher_query(query, {'id': str(id)})
        user = results[0][0]
        user = User.inflate(user)
        query = """
        MATCH (r:Review)
        RETURN MAX(r.review_id)
        """
        results, _ = db.cypher_query(query, {'id': str(id)})
        review_id = int(results[0][0])+1
        new_review = Review(comments=review_text, user=user, listings=listing, date=datetime.now().strftime('%Y-%m-%d'), review_id=review_id)
        new_review.save()

        messages.success(request, 'Review added successfully!')
        return redirect('/review/'+ str(listing_id))
    
    query = """
    MATCH (a:User)
    RETURN a
    """
    user_results, _ = db.cypher_query(query)
    users = [User.inflate(row[0]) for row in user_results[:10]]
    return render(request, 'create/review.html', {
        'users': users,
        'listing': listing,
        'STATIC_URL':settings.STATIC_URL
        })
    
def getAllAmenities(request):
    query = """
    MATCH (a:Amenity)
    RETURN (a)
    """
    amenity_results, _ = db.cypher_query(query)
    amenities = [Amenity.inflate(row[0]).name for row in amenity_results]

    return render(request, 'filter.html', {
        'amenities': amenities,
        'STATIC_URL': settings.STATIC_URL
    })

def resultFilter(request):
    
    amenities = []
    amenity1 = request.GET.get('amenity1')
    if amenity1 != '':
        amenities.append(amenity1)
    amenity2 = request.GET.get('amenity2')
    if amenity2 != '':
        amenities.append(amenity2)
    amenity3 = request.GET.get('amenity3')
    if amenity3 != '':
        amenities.append(amenity3)
    if amenities == []:
        return redirect('/listings/1')
    query = """
    MATCH (a:Amenity)-[:HAS]-(l:Listing)
    WHERE a.name IN $amenities
    RETURN DISTINCT l
    """
    listing_results, _ = db.cypher_query(query, {
        'amenities': amenities
    })
    listings = [Listing.inflate(row[0]) for row in listing_results]
    return render(request, 'results.html', {
        'listing': listings,
        'total': len(listings),
        'STATIC_URL': settings.STATIC_URL
    })
