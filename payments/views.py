from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy


from payments.models import Payment
from projects.models import Project
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
    fields = ["project","amount","due_date","status"]
    template_name = "payments/payment_update_form.html"
    context_object_name = "payment"

    def get_success_url(self):
        return reverse_lazy("payments:detail", kwargs={"pk":self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()  # pass clients for dropdown
        return context


class PaymentDetailView(DetailView):
    model = Payment
    template_name = "payments/payment_detail.html"
    context_object_name = "payment"


class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = "payments/payment_delete_confirm.html"
    success_url = reverse_lazy("payments:list")
    context_object_name = "payment"



