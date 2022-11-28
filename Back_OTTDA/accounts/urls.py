from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import AuthView, RegisterAPIView

urlpatterns = [
    # path("", include(router.urls)),
    path("register/", RegisterAPIView.as_view()), #회원가입하기
    path("auth/", AuthView.as_view()), #로그인하기
    path('auth/refresh/', TokenRefreshView.as_view()),#토큰 재발급하기
]