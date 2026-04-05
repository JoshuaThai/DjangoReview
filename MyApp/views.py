from gc import get_objects

from django.db.models import Model
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ticket

# Create your views here.
def home(request):
    if request.method == "POST":
        dayOfWeek = request.POST.get("week")
        date_time = request.POST.get("date-time")
        location = request.POST.get("location")
        # This immediately saves the new ticket to the database
        new_ticket = Ticket.objects.create(
            week=dayOfWeek,
            date_time=date_time,
            location=location
        )
        new_ticket.save()
        tickets = Ticket.objects.all()
        return render(request, "tickets.html", {"tickets": tickets})

    template = loader.get_template('home.html')
    return HttpResponse(template.render())