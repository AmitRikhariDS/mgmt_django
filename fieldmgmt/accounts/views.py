from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group, User

def landing(request):
    """Landing page with stakeholder registration links"""
    return render(request, "landing.html")

def register_view(request, role=None):
    """Register a user with optional role assignment"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign role if provided
            if role:
                group, created = Group.objects.get_or_create(name=role)
                user.groups.add(group)
            login(request, user)
            return redirect("jobs:job_list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form, "role": role})
