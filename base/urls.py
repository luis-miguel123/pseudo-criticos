
from django.urls import path
from base.views import homeView


urlpatterns = [
    
    path('home/', homeView.as_view())
]