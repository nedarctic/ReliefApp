from django.urls import path
from .views import DisasterListCreateView, DisasterDetailView, SafeZoneListCreateView, SafeZoneDetailView, UpdateListCreateView, UpdateDetailView

urlpatterns = [
    path('disasters/', DisasterListCreateView.as_view(), name='disaster-list-create'),
    path('disasters/<int:pk>/', DisasterDetailView.as_view(), name='disaster-detail'),
    path('safezones/', SafeZoneListCreateView.as_view(), name='safezone-list-create'),
    path('safezones/<int:pk>/', SafeZoneDetailView.as_view(), name='safezone-detail'),
    path('updates/', UpdateListCreateView.as_view(), name='update-list-create'),
    path('updates/<int:pk>/', UpdateDetailView.as_view(), name='update-detail'),
]