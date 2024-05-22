from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking
from .forms import BookingForm

def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})

def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'events/book_event.html', {'event': event, 'form': form})
