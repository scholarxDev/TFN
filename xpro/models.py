from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.db import models
from organizations.models import Organization, OrganizationAwareModel


# Create your models here.
class User(AbstractUser):
	GENDER_CHOICES = (
		('O', 'Other'),
		('M', 'Male'),
		('F', 'Female'),
	)

	is_student = models.BooleanField(default=False)
	is_school = models.BooleanField(default=False)
	is_sponsor = models.BooleanField(default=False)
	email = models.EmailField(unique=True)
	email_confirmed = models.BooleanField(default=False)
	phone_number = models.CharField(max_length=12)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, editable=False)
	# avatar = models.ImageField(upload_to='media/avarta', blank=True, default= '/media/avarta/default.png', null=True,)

	def __str__(self):
		return self.email


class Student(OrganizationAwareModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='student')
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	address = models.CharField(max_length=255, blank=True)
	country = CountryField(blank_label='select country')
	career_aspiration = models.CharField(max_length=255, blank=True)
	role_model = models.CharField(max_length=255, blank=True)
	current_academic_level = models.CharField(max_length=255, blank=True)
	school_name = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return f'{self.user.username} student'


class School(OrganizationAwareModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='school')
	school_name = models.CharField(max_length=100, blank=True)
	address = models.CharField(max_length=255, blank=True)
	country = CountryField(blank_label='select country')
	state = models.CharField(max_length=30, blank=True)
	
	def __str__(self):
		return f'{self.user.username} school'


class Sponsor(OrganizationAwareModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='sponsor')
	is_anonymous = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.user.username} sponsor'

