
from django.db import models 
from django_countries.fields import CountryField
from organizations.models import OrganizationAwareModel


# Create your models here.
class Category(OrganizationAwareModel):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class College(OrganizationAwareModel):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name


class Scholarship(OrganizationAwareModel):
	name = models.CharField(max_length=555)
	country = CountryField(blank_label='select country')
	college = models.ManyToManyField('College', related_name='college')
	award = models.CharField(max_length=255)
	website = models.URLField(max_length=250)
	deadline = models.DateTimeField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category', related_name='category')

	def __str__(self):
		return self.name
