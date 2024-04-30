"""airbnb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from listing import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='index'),
    path('', views.index, name='index'),
    path('listings/<int:pag>/', views.listListing, name='index'),
    path('hosts/<int:pag>/', views.listHost, name='index'),
    path('neighborhoods/<int:pag>/', views.listNeighborhood, name='index'),
    path('amenities/<int:pag>/', views.listAmenity, name='index'),
    path('users/<int:pag>/', views.listUser, name='index'),
    path('reviews/<int:pag>/', views.listReview, name='index'),
    path('listing/<int:id>/', views.getListing, name='index'),
    path('host/<int:id>/', views.getHost, name='index'),
    path('neighborhood/<int:id>/', views.getNeighborhood, name='index'),
    path('amenity/<str:id>/', views.getAmenity, name='index'),
    path('user/<int:id>/', views.getUser, name='index'),
    path('review/<int:id>/', views.getReview, name='index'),
    path('mostRated/', views.getMostRatedListing, name='index'),
    path('filterByAmenities/', views.getAllAmenities, name='index'),
    path('results/', views.resultFilter, name='index'),
]
