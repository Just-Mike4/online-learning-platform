# views.py
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer, LoginSerializer
from django.contrib.auth import authenticate

# Registration Views
class BaseRegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer
    role = None  # To be defined in subclasses

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(role=self.role)
        return Response(
            {"message": f"{self.role.capitalize()} registration successful. You can login now."},
            status=status.HTTP_201_CREATED
        )

class InstructorRegistrationView(BaseRegistrationView):
    role = 'instructor'

class AdminRegistrationView(BaseRegistrationView):
    role = 'admin'

class StudentRegistrationView(BaseRegistrationView):
    role = 'student'

# Login Views
class BaseLoginView(APIView):
    role = None  # To be defined in subclasses

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            if user:
                if user.role != self.role:
                    return Response(
                        {"error": f"Access restricted to {self.role}s only"},
                        status=status.HTTP_403_FORBIDDEN
                    )
                refresh = RefreshToken.for_user(user)
                return Response({"access": str(refresh.access_token)}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstructorLoginView(BaseLoginView):
    role = 'instructor'

class AdminLoginView(BaseLoginView):
    role = 'admin'

class StudentLoginView(BaseLoginView):
    role = 'student'