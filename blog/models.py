
from django.db import models 
from django.utils import timezone
from organizations.models import OrganizationAwareModel


# Create your models here. 

class Category(OrganizationAwareModel):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Post(OrganizationAwareModel):
	title = models.CharField(max_length=255)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category', related_name='posts')

	def __str__(self):
		return self.title

	class Meta:
		default_permissions = ('add',)
		permissions = (
			('read', 'Can read'),
		)


class Comment(models.Model):
	author = models.CharField(max_length=60)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)

	def __str__(self):
		return self.author
