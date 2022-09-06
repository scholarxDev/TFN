from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import *


class StudentSignUpForm(UserCreationForm):
	"""A form that creates a Student user, from the given email and password. """
	first_name = forms.CharField(max_length=30, required=True, help_text='First name is required.')
	last_name = forms.CharField(max_length=30, required=True, help_text='Last name is required.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'phone_number',)

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_student = True
		user.save()
		student = Student.objects.create(user=user)
		return user


class StudentChangeForm(forms.ModelForm):
	"""A form for updating users. Includes all the fields on the user, but replaces
	the password field with admin's password hash display field. """

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'gender', 'phone_number',)


class StudentProfileForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('bio', 'birth_date', 'address', 'country', 'career_aspiration', 'role_model', 'current_academic_level', 'school_name', 'country')

	def clean_avatar(self):
		avatar = self.cleaned_data['avatar']

		try:
			w, h = get_image_dimensions(avatar)

			# validate dimensions
			max_width = max_height = 100
			if w > max_width or h > max_height:
				raise forms.ValidationError(
					u'Please use an image that is '
					'%s x %s pixels or smaller.' % (max_width, max_height))

			# validate content type
			main, sub = avatar.content_type.split('/')
			if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
				raise forms.ValidationError(u'Please use a JPEG, '
											'GIF or PNG image.')

			# validate file size
			if len(avatar) > (20 * 1024):
				raise forms.ValidationError(
					u'Avatar file size may not exceed 20k.')

		except AttributeError:
			"""
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
			pass

		return avatar

class TfnStudentProfileForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('bio', 'birth_date', 'address', 'country', 'country')

	def clean_avatar(self):
		avatar = self.cleaned_data['avatar']

		try:
			w, h = get_image_dimensions(avatar)

			# validate dimensions
			max_width = max_height = 100
			if w > max_width or h > max_height:
				raise forms.ValidationError(
					u'Please use an image that is '
					'%s x %s pixels or smaller.' % (max_width, max_height))

			# validate content type
			main, sub = avatar.content_type.split('/')
			if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
				raise forms.ValidationError(u'Please use a JPEG, '
											'GIF or PNG image.')

			# validate file size
			if len(avatar) > (20 * 1024):
				raise forms.ValidationError(
					u'Avatar file size may not exceed 20k.')

		except AttributeError:
			"""
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
			pass

		return avatar


class SchoolSignUpForm(UserCreationForm):
	"""A form that creates a School user, with no privileges, from the given email and password. """
	school_name = forms.CharField(max_length=100, required=True, help_text='School name is required.')

	class Meta:
		model = User
		fields = ('username', 'school_name', 'email', 'phone_number',)
	
	@transaction.atomic
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_school = True
		user.save()
		school = School.objects.create(user=user)
		return user


class SchoolChangeForm(UserChangeForm):
	"""A form for updating users. Includes all the fields on the user, but replaces the
	password field with admin's password hash display field. """

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class SchoolProfileForm(UserChangeForm):
	
	class Meta:
		model = School
		fields = ('address', 'state', 'country', 'school_name')


class SponsorSignUpForm(UserCreationForm):
	"""A form that creates a Sponsor user, with no privileges, from the given email and password. """
	first_name = forms.CharField(max_length=30, required=True, help_text='First name is required')
	last_name = forms.CharField(max_length=30, required=True, help_text='Last name is required')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'phone_number',)
	
	@transaction.atomic
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_sponsor = True
		user.save()
		sponsor = Sponsor.objects.create(user=user)
		return user


class SponsorChangeForm(UserChangeForm):
	"""A form for updating users. Includes all the fields on the user, but replaces the
	password field with admin's password hash display field. """

	class Meta:
		model = User
		fields = ('username', 'email')


class SponsorProfileForm(forms.ModelForm):
	address = forms.CharField(max_length=255)
	state = forms.CharField(max_length=30)

	class Meta:
		model = Sponsor
		fields = ('address', 'state',)


class CustomUserCreationForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

	class Meta(UserCreationForm):
		model = User
		fields = ('username', 'email', 'phone_number',)


class CustomUserChangeForm(UserChangeForm):
	"""A form for updating users. Includes all the fields on the user,
	but replaces the password field with admin's password hash display field. """

	class Meta:
		model = User
		fields = ('username', 'email', 'phone_number',)
