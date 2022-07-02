
from django.urls import path
from base.views import homeView, loginView


urlpatterns = [
    
    path('home/', homeView.as_view()),
    path('login/', loginView.as_view())
]