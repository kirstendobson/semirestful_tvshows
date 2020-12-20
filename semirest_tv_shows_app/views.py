from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Show

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def shows_new(request):
    return render(request, 'shows_new.html')

def create_show(request):
    errors = Show.objects.show_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    new_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        desc=request.POST['desc']
    )
    return redirect(f'/shows/{ new_show.id }')

def view_show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show,
    }    
    return render(request, 'view_show.html', context)

def edit_show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show,
    }
    return render(request, 'edit_show.html', context)

def update_show(request, show_id):
    errors = Show.objects.show_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    show_update = Show.objects.get(id=show_id)
    show_update.title = request.POST['title']
    show_update.release_date = request.POST['release_date']
    show_update.network = request.POST['network']
    show_update.desc = request.POST['desc']
    show_update.save()

    return redirect(f'/shows/{show_id}')

def delete_show(request, show_id):
    show_delete = Show.objects.get(id=show_id)
    show_delete.delete()
    return redirect('/shows')