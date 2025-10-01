from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import UpdateView, DetailView, DeleteView



from clients.models import Client
from clients.forms import ClientForm

# Create your views here.
def client_list(request):
    clients = Client.objects.all()
    return render(request, "clients/client_list.html", {"clients":clients})

@csrf_protect
def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:index")
        else:
            print("FORM ERRORS", form.errors)
            return redirect("dashboard:index")
    return redirect("dashboard:index")

class ClientDetailView(DetailView):
    model = Client
    template_name = "clients/client_detail.html"
    context_object_name = "client"

class ClientUpdateView(UpdateView):
    model = Client
    fields = ["name", "email", "phone_no","company"]
    template_name = "clients/client_update_form.html"
    context_object_name = "client"

    def get_success_url(self):
        return reverse_lazy("clients:detail", kwargs={"pk": self.object.pk})

