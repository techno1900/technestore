from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name="store"),
    path("filter-by-category/<str:category_name>/", views.store, name="filter-by-category"),
    path("single-product/<str:pk>/", views.single_product, name="single-product"),
    path('search/', views.search, name="search"),
]
