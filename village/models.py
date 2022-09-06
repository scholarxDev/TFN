from django.db import models
from django.contrib.auth import get_user_model
from organizations.models import OrganizationAwareModel


# Create your models here.
class Village(OrganizationAwareModel):
	fund_request_count = models.IntegerField(default=429)
	total_amount_raised = models.IntegerField(default=6691263)
	fully_funded = models.IntegerField(default=131)


class FundRequest(OrganizationAwareModel):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	request_title = models.CharField(max_length=255)
	How_much_do_you_need = models.IntegerField(default=0)
	Tell_us_why_you_need_it = models.TextField()
	How_soon_do_you_need_it = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	request_confirmed = models.BooleanField(default=False)
	amount_raised = models.IntegerField(default=0)
	percentage_raised = models.IntegerField(default=0)
	complete = models.BooleanField(default=False)
	
	class Meta:
		
		permissions = (
			('view_request', 'Can view request'),
			("can_approve_request", "Can approve a request"),
		)
	
	def __str__(self):
		return f'{self.user.username} fundrequest'


class Comment(OrganizationAwareModel):
	name = models.CharField(max_length=60)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	request = models.ForeignKey('FundRequest', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user.username} comment'
