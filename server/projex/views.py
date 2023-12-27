from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializer import UserSerializer, PreferenceSerializer, GenerationSerializer, SavedProjectSerializer
from .models import User, Preference, Generation, SavedProject


def members(request):
    return HttpResponse("Hello world!")