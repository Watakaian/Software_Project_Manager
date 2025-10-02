from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, DeleteView, UpdateView


from payments.models import Payment
from payments.forms import PaymentForm

# Create your views here.
def payments_list(request):
    payments = Payment.objects.all()
    return render(request, "payments/payment_list.html", {"payments":payments})

@csrf_protect
def create_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:index")
        else:
            print("FORM ERRORS", form.errors)
            return redirect("dashboard:index")
    return redirect("dashboard:index")


class PaymentUpdateView(UpdateView):
    model = Payment
    template_name = "TEMPLATE_NAME"
    context_object_name = "payment"


class PaymentDetailView(DetailView):
    model = Payment
    template_name = "TEMPLATE_NAME"
    context_object_name = "payment"



class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = "TEMPLATE_NAME"
    context_object_name = "payment"



