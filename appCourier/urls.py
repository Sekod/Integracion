from django.urls import path
from .views import SolicitudListView, SolicitudDetailView

urlpatterns = [
    path('solicitud/', SolicitudListView.as_view(), name='Solicitud-list'),
    path('solicitud/<int:codigo>/', SolicitudDetailView.as_view(), name='Solicitud-detail'),
  ]
    