from apps.base.models import AuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomTokenAuthentication(TokenAuthentication):
    model = AuthToken


class IrbaseAPIView(APIView):
    authentication_classes = [CustomTokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TokenRegistrationService:

    def __init__(self):
        super(TokenRegistrationService, self).__init__()

    def register(self, user):
        token = AuthToken.objects.create(user=user)
        return token.key

    def deregister(self, key):
        AuthToken.objects.first(key=key).delete()


class TokenMixingService:

    def __init__(self):
        super(TokenMixingService, self).__init__()

    def __delete_token(self, token):
        token_service = TokenRegistrationService()
        token_service.deregister(token)