from django.urls import path
from clients import views

app_name = "clients"

urlpatterns = [
    path("", views.client_list, name="list"),
    path("client/create/", views.create_client, name="create"),
]
