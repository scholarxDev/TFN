from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import CampaignForm

# Create your views here.


def campaign(request):
  
    return render(request, "campaign/index.html", {})


@login_required
@user_passes_test(lambda u: u.is_sponsor)
def create(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            # title = form.cleaned_data.get('title')
            # objective = form.cleaned_data.get('objective')
            # duration = form.cleaned_data.get('duration')


            return redirect('sponsor-dashboard')

    else:
        form = CampaignForm()
   
    return render(request, "campaign/create.html", {'form': form})

