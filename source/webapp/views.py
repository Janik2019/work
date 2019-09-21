from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Entry, status_choices
from webapp.forms import guestbookForm

def guestbook_index(request, *args, **kwargs):
    guestbook = Entry.objects.order_by('-date').filter(status='active')
    return render(request, 'index.html', context={
        'guestbook': guestbook,
    })


def guestbook_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = guestbookForm()
        return render(request, 'guestbookcreate.html', context={'form': form})
    elif request.method == 'POST':
        form = guestbookForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            guestbook = Entry.objects.create(name=data['name'], email=data['email'],text=data['text'])
            return redirect('index')
        else:
            return render(request, 'guestbookcreate.html', context={'form': form})