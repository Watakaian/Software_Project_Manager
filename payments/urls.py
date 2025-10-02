from django.urls import path
from payments import views

app_name = "payments"

urlpatterns = [
    path("",views.payments_list, name="list"),
    path("payment/create/", views.create_payment, name="create"),
    path("<int:pk>/", views.PaymentDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.PaymentDeleteView.as_view(), name="delete"),
    path("<int:pk>/edit/", views.PaymentUpdateView.as_view(), name="edit"),
]