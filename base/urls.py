from django.contrib import admin
from django.urls import path
from base.views import homeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homeView)
]