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


def guestbook_edit(request, pk):
    guestbook = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        form = guestbookForm(data={'name': guestbook.name,
                              'email': guestbook.email,
                              'status': guestbook.text
                              })
        return render(request, 'guestbook_edit.html', context={'form': form, 'guestbook': guestbook})
    elif request.method == 'POST':
        form = guestbookForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            guestbook.name = data['name']
            guestbook.email = data['email']
            guestbook.text = data['text']
            guestbook.save()
            return redirect('index')
        else:
            return render(request, 'guestbook_edit.html', context={'form': form, 'guestbook': guestbook})


def guestbook_delete(request, pk):
    guestbook = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        return render(request, 'guestbook_delete.html', context={'guestbook': guestbook})
    elif request.method == 'POST':
        guestbook.delete()
        return redirect('index')



def search(request):
    print(request.GET)
    list=request.GET.get('search')
    guests= Entry.objects.filter(name__contains=list)
    return render(request, 'index.html', context={
        'guestbook': guests
    })