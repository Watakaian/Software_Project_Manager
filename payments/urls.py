from django.urls import path
from payments import views

app_name = "payments"

urlpatterns = [
    path("",views.payments_list, name="list"),
    path("payment/create/", views.create_payment, name="create")
]