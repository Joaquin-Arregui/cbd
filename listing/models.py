from django_neomodel import DjangoNode
from neomodel import (StructuredNode, StringProperty, BooleanProperty, FloatProperty,
                      IntegerProperty, RelationshipTo, RelationshipFrom, UniqueIdProperty)

class Amenity(DjangoNode):
    name = StringProperty(unique_index=True, required=True)

    listings = RelationshipFrom('Listing', 'HAS')
    class Meta:
        app_label = 'listing'

class Neighborhood(DjangoNode):
    name = StringProperty()
    neighborhood_id = StringProperty(unique_index=True, required=True)

    listings = RelationshipFrom('Listing', 'IN_NEIGHBORHOOD')
    class Meta:
        app_label = 'listing'

class Host(DjangoNode):
    name = StringProperty()
    host_id = StringProperty(unique_index=True, required=True)
    superhost = BooleanProperty(required=True)
    location = StringProperty()
    image = StringProperty()

    listings = RelationshipTo('Listing', 'HOSTS')
    class Meta:
        app_label = 'listing'

class User(DjangoNode):
    name = StringProperty(required=True)
    user_id = StringProperty(unique_index=True, required=True)
    
    reviews = RelationshipTo('Review', 'WROTE')
    class Meta:
        app_label = 'listing'

class Review(DjangoNode):
    review_id = StringProperty(unique_index=True, required=True)
    date = StringProperty(required=True)
    comments = StringProperty(required=True)
    
    listings = RelationshipTo('Listing', 'REVIEWS')
    user = RelationshipFrom('User', 'WROTE')
    class Meta:
        app_label = 'listing'

class Listing(DjangoNode):
    listing_id = StringProperty(unique_index=True, required=True)
    name = StringProperty(required=True)
    price = FloatProperty()
    property_type = StringProperty(required=True)
    accommodates = IntegerProperty(required=True)
    bedrooms = IntegerProperty()
    bathrooms = IntegerProperty()
    availability_365 = IntegerProperty(required=True)
    weekly_price = FloatProperty()
    cleaning_fee = FloatProperty()

    class Meta:
        app_label = 'listing'

    # Relationships
    amenities = RelationshipTo('Amenity', 'HAS')
    neighborhood = RelationshipTo('Neighborhood', 'IN_NEIGHBORHOOD')
    host = RelationshipFrom('Host', 'HOSTS')
    reviews = RelationshipFrom('Review', 'REVIEWS')