from django.db import models
from django.contrib.auth import get_user_model
from organizations.models import OrganizationAwareModel


# Create your models here.

class Payment(OrganizationAwareModel):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	ref_id = models.IntegerField()
	amount = models.IntegerField()
	email = models.EmailField()
	meta_data = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
			return f'{self.user.username} payment'


