from django.urls import path
from clients import views

app_name = "clients"

urlpatterns = [
    path("", views.client_list, name="list"),
    path("client/create/", views.create_client, name="create"),
    path("<int:pk>/", views.ClientDetailView.as_view(),name="detail"),
    path("<int:pk>/edit/", views.ClientUpdateView.as_view(),name="edit"),
    path("<int:pk>/delete/", views.ClientDeleteView.as_view(),name="delete"),
]
