from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def redirect_dashboard(request):
    return redirect("dashboard:index")