from bridger.filters import FilterSet
from bridger.viewsets import ModelViewSet, RepresentationViewSet
from django.http import Http404
from rest_framework.decorators import action
from rest_framework.response import Response

from .button.to_do import ToDoButtonConfig
from .display.religion import ReligionDisplayConfig
from .display.to_do import ToDoDisplayConfig
from .models import Religion, Student
from .serializers import (ReligionRepresentationSerializer, ReligionSerializer,
                          StudentSerializer)

# from rest_framework import status, viewsets
# from rest_framework.response import Response
# from rest_framework.views import APIView




class StudentDetail(ModelViewSet):
    display_config_class = ToDoDisplayConfig
    button_config_class = ToDoButtonConfig
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class ReligionRepresentationViewSet(RepresentationViewSet):
    queryset = Religion.objects.all()
    serializer_class = ReligionRepresentationSerializer
    

class ReligionViewSet(ModelViewSet):
    display_config_class = ReligionDisplayConfig
    # title_config_class = ReligionTitleConfig
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer


