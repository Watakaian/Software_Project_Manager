from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("", views.project_list, name="list"),
    path("<int:pk>/delete/", views.project_delete, name="delete"),
    path("<int:pk>/update-inline/", views.project_update_inline, name="update_inline"),
]
