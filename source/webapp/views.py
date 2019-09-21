from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Entry, status_choices

def guestbook_index(request, *args, **kwargs):
    guestbook = Entry.objects.order_by('-date').filter(status='active')
    return render(request, 'index.html', context={
        'guestbook': guestbook,
    })
