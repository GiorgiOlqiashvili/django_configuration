from django.urls import path
from .views import AnimalCreateView, AnimalDeleteView, AnimalDetailView

urlpatterns = [
    path('create/', AnimalCreateView.as_view(), name='animal-create'),
    path('<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
    path('<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal-delete'),
]
