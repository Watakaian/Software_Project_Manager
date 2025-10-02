from django.urls import path
from projects import views

app_name = "projects"

urlpatterns = [
    #projects
    path("", views.project_list, name="list"),
    path("project/create/", views.create_project, name="create"),
    path("<int:pk>/",views.ProjectDetailView.as_view(),name="detail"),
    path("<int:pk>/delete/", views.ProjectDeleteView.as_view(), name="delete"),
    path("<int:pk>/edit/", views.ProjectUpdateView.as_view(), name="update"),

    # requirements
    path("requirement_list/", views.requirement_list, name="requirement_list"),
    path("requirement/create/", views.create_requirement, name="create_requirement"),
    path("requirement/<int:pk>/",views.RequirementDetailView.as_view(), name="requirement_detail"),
    path("requirement/<int:pk>/delete/", views.RequirementDeleteView.as_view(), name="delete_requirement")
]
