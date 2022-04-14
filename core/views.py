from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
  return render(request, 'home.html')

@login_required(login_url="/accounts/login/")
def dashboard(request):
  return render(request, 'dashboard/index.html')

@login_required(login_url="/accounts/login/")
def profile(request):
  return render(request, 'account/profile.html')

