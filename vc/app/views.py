from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def login(request):
    # Your login view logic here
    return HttpResponse("Login Page")

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving the profile data
    else:
        form = ProfileForm(instance=user.profile)

    context = {
        'form': form,
    }
    return render(request, 'app/profile.html', context)



