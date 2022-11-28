from django.urls import path
from . import views


urlpatterns = [
    path('', views.popular_movie_json),
    path('tv/',views.popular_tv_json),
    path('movieprovider/<int:movie_id>/', views.movie_provider_json),
    path('tvprovider/<int:tv_id>/', views.tv_provider_json),
    path('search/<str:title>/', views.search_multi_json),
    path('moviedetail/<int:movie_id>/', views.movie_detail_json),
    path('tvdetail/<int:tv_id>/', views.tv_detail_json),
    path('al/', views.recoott),
    path('staraverage/<int:movie_id>/', views.star_average_json)

]
