from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from apps.users.views import (
    UserListCreateAPIView,
    LoginAPIView,
    LogoutAPIView
)


urlpatterns = [
    path('create/', UserListCreateAPIView.as_view(), name="create"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/', TokenRefreshView.as_view(), name='token_refresh'),

]