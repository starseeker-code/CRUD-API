from django.contrib import admin
from django.urls import path
import ninja
from library_api.application import router as service

api = ninja.NinjaAPI()
api.add_router("/", service, tags=["Service"])

urlpatterns = [
    path('', api.urls),
]
