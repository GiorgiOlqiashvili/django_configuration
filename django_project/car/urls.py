from django.urls import path
from .views import CarCreateView, CarDeleteView, CarDetailView

urlpatterns = [
    path('create/', CarCreateView.as_view(), name='car-create'),
    path('<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
]
