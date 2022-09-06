from django import forms
from .models import Campaign 
from django.db import transaction

class CampaignForm(forms.ModelForm):

	title = forms.CharField(max_length=255)
	campaign_objective = forms.CharField(widget=forms.Textarea)
	duration = forms.CharField(max_length=255)

	class Meta:
		model = Campaign
		fields =  ('title','campaign_objective', 'duration',)

	
