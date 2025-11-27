from .serializers import UserSerializer
from rest_framework.decorators import api_view

def user_registration(request):
    serializer = UserSerializer(data=request.data)
    pass