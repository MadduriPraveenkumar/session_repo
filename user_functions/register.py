from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



def user_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user = User.objects.create_user(**serializer.validated_data)
            return Response({"id": user.id}, status=status.HTTP_201_CREATED)
        except:
            pass
    pass