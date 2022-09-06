from django import forms
from .models import FundRequest

class FundRequestForm(forms.ModelForm):

	class Meta:
		model = FundRequest
		fields =  ('request_title','How_much_do_you_need','Tell_us_why_you_need_it', 'How_soon_do_you_need_it',)

class TfnFundRequestForm(forms.ModelForm):
	PROJECTS = (
		("Health based initiatives", "Health based initiatives"),
		("STEM projects", "STEM projects"),
		("Teacher training, literacy and numeracy advancement projects", "Teacher training, literacy and numeracy advancement projects"),
		("WASH Projects ( Education on menstrual health and hygiene, Provision of sanitary towels, build/renovation of toilets with water supply)",
		 "WASH Projects ( Education on menstrual health and hygiene, Provision of sanitary towels, build/renovation of toilets with water supply)"),
		("COVID 19 intervention projects", "COVID 19 intervention projects"),
		("Renovation projects", "Renovation projects"),
		("Community empowerment projects", "Community empowerment projects"),
	)
	request_title = forms.ChoiceField(choices=PROJECTS, required=True, label="Project title")

	class Meta:
		model = FundRequest
		fields =  ('request_title','How_much_do_you_need','Tell_us_why_you_need_it', 'How_soon_do_you_need_it')
		labels = {
			"Tell_us_why_you_need_it": "Tell us the project location, project summary, challenges and solution",
		}
		widgets = {
            'Tell_us_why_you_need_it':forms.Textarea(
				attrs={'placeholder': "Project Location:\n\nProject Summary:\n\nChallenges:\n\nSolutions:\n\n"}),

        }



	
