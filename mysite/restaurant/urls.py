from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainAPIView.as_view(), name='main')
]
