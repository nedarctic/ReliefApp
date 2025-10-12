from .serializers import DisasterSerializer, SafeZoneSerializer, UpdateSerializer
from .models import Disaster, SafeZone, Update

from rest_framework import generics

class DisasterListCreateView(generics.ListCreateAPIView):
    queryset = Disaster.objects.all()
    serializer_class = DisasterSerializer
    
class DisasterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disaster.objects.all()
    serializer_class = DisasterSerializer
    
class SafeZoneListCreateView(generics.ListCreateAPIView):
    queryset = SafeZone.objects.all()
    serializer_class = SafeZoneSerializer
    
class SafeZoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SafeZone.objects.all()
    serializer_class = SafeZoneSerializer
    
class UpdateListCreateView(generics.ListCreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    
class UpdateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer