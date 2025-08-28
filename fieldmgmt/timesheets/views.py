from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Timesheet
from .forms import TimesheetForm

@login_required
def timesheet_list(request):
    """List all timesheets for the logged-in user"""
    timesheets = Timesheet.objects.filter(user=request.user)
    return render(request, "timesheets/timesheet_list.html", {"timesheets": timesheets})

@login_required
def timesheet_create(request):
    """Create a new timesheet entry"""
    if request.method == "POST":
        form = TimesheetForm(request.POST)
        if form.is_valid():
            ts = form.save(commit=False)
            ts.user = request.user
            ts.save()
            return redirect("timesheets:timesheet_list")
    else:
        form = TimesheetForm()
    return render(request, "timesheets/timesheet_form.html", {"form": form})
