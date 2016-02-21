from rest_framework import generics
from .serializers import *

class AuthorView(generics.ListAPIView):

    """
    Returns a list of all authors.
    """
    model = Author
    serializer_class = AuthorSerializer
