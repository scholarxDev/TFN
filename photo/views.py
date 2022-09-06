from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Photo
from .forms import PhotoForm


# Create your views here.

@login_required
@transaction.atomic
def upload(request, pk=None):
    instance = Photo.objects.get(pk=pk) if pk else None
    context = dict(save_pk=pk or "")
    if request.method == 'POST':
        # Only backend upload should be posting here
        context['backend_form'] = form = PhotoForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            # Uploads image and creates a model instance for it
            context['posted'] = form.save(commit=False)
            context['posted'].user = request.user
            context['posted'].save()

        instance = Photo.objects.get(pk=pk) if pk else None
    else:
        # Form demonstrating backend upload
        context['backend_form'] = PhotoForm(instance=instance)

    return render(request, 'photo/upload.html', context)


