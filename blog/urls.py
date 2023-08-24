from django.contrib import admin
from django.urls import path
from posts.api import api
#from ninja import NinjaAPI

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', api.urls)
]
