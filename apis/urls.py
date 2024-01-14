from django.urls import path
from .views import ClientLists, ClientCreate, ClientsData

urlpatterns = [
    path('clients/', ClientLists.as_view(), name='client-list'),
    path('create-client/', ClientCreate.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientsData.as_view(), name='client-list-create'),
]
