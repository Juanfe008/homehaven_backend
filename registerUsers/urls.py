from django.urls import path
from .views import ItemList, ItemDetail

urlpatterns = [
    path('register/', ItemList.as_view(), name='register-user'),
]