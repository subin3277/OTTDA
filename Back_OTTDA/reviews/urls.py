from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('reviews/<int:review_pk>/comments/', views.comment_create),
    path('recomments/', views.recomment_list),
    path('recomments/<int:recomment_pk>/', views.recomment_detail),
    path('comments/<int:comment_pk>/recomments/', views.recomment_create),
    path('reviewsearch/<int:movie_id>/', views.search_review_json),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
