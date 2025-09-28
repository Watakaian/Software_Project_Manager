from django.urls import path
from projects import views

app_name = "projects"

urlpatterns = [
    path("", views.project_list, name="list"),
    path("project/create/", views.create_project, name="create"),
    path("<int:pk>/",views.ProjectDetailView.as_view(),name="detail"),
    path("<int:pk>/delete/", views.ProjectDeleteView.as_view(), name="delete"),
    path("<int:pk>/edit/", views.ProjectUpdateView.as_view(), name="update"),
]
