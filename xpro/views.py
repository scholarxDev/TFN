from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.template.loader import render_to_string
from .models import User
from village.models import FundRequest
from scholarship.models import Scholarship
from .forms import StudentSignUpForm, StudentChangeForm, StudentProfileForm, SchoolSignUpForm, SchoolChangeForm, \
    SchoolProfileForm, SponsorSignUpForm, SponsorChangeForm, SponsorProfileForm, TfnStudentProfileForm
from .tokens import account_activation_token
from django.db import transaction


# Create your views here.
def index(request):

    scholarships = Scholarship.objects.filter(
        organization=request.organization).order_by('-created_on')[:3]

    return render(request, 'xpro/index.html', {'scholarships': scholarships, })


def about(request):

    return render(request, 'xpro/about.html', {})


def signup(request):

    return render(request, 'registration/signup.html', {})


def activation_sent(request):

    return render(request, 'registration/activation_sent.html', {})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    else:
        return render(request, 'registration/activation_invalid.html')


def student(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            print(request.organization)
            user.organization = request.organization
            user.save()
            print(f"Checking user's org:{user.organization}")
            current_site = get_current_site(request)
            subject = 'Activate Your ScholarX Account'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')

    else:
        form = StudentSignUpForm()
    return render(request, 'registration/student.html', {'form': form})


@user_passes_test(lambda u: u.is_student)
def studentDashboard(request):
    scholarships = Scholarship.objects.filter(organization=request.organization).order_by('-created_on')[:3]

    return render(request, 'xpro/student/dashboard.html', {'scholarships': scholarships, })


@user_passes_test(lambda u: u.is_student)
def studentProfile(request):

    return render(request, 'xpro/student/profile.html', {'user': request.user})


@transaction.atomic
@user_passes_test(lambda u: u.is_student)
def editStudentProfile(request):
    profile_form = StudentProfileForm if request.organization.name == "scholarx" else TfnStudentProfileForm
    if request.method == 'POST':
        user_form = StudentChangeForm(request.POST, request.FILES, instance=request.user)
        form = profile_form(request.POST, instance=request.user.student)
        if user_form.is_valid() and form.is_valid():
            user_form.save()
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('student-profile')

        else:
            messages.error(request, 'Please correct the error below.')

    else:
        user_form = StudentChangeForm(instance=request.user)
        form = profile_form(instance=request.user.student)

    return render(request, 'xpro/student/edit_profile.html', {
        'user_form': user_form,
        'form': form
    })


def school(request):
    if request.method == 'POST':
        form = SchoolSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.organization = request.organization
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your ScholarX Account'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')

    else:
        form = SchoolSignUpForm()
    return render(request, 'registration/school.html', {'form': form})


@user_passes_test(lambda u: u.is_school)
def schoolDashboard(request):
    scholarships = Scholarship.objects.filter(organization=request.organization).order_by('-created_on')[:3]

    return render(request, 'xpro/school/dashboard.html', {"scholarships": scholarships, })


@user_passes_test(lambda u: u.is_school)
def schoolProfile(request):

    return render(request, 'xpro/school/profile.html', { 'user': request.user})


@transaction.atomic
@user_passes_test(lambda u: u.is_school)
def editSchoolProfile(request):
    if request.method == 'POST':
        user_form = SchoolChangeForm(request.POST, instance=request.user)
        school_form = SchoolProfileForm(request.POST, instance=request.user.school)
        if user_form.is_valid() and school_form.is_valid():
            user_form.save()
            school_form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('school-profile')
        else:
            messages.error(request, ('Please correct the error below.'))

    else:
        user_form = SchoolChangeForm(instance=request.user)
        school_form = SchoolProfileForm(instance=request.user.school)

    return render(request, 'xpro/school/edit_profile.html', {
        'user_form': user_form,
        'school_form': school_form
    })


def sponsor(request):
    if request.method == 'POST':
        form = SponsorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.organization = request.organization
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your ScholarX Account'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SponsorSignUpForm()
    return render(request, 'registration/sponsor.html', {'form': form})


@user_passes_test(lambda u: u.is_sponsor)
def sponsorSuccess(request):

    return render(request, 'xpro/sponsor/success.html', {})


@user_passes_test(lambda u: u.is_sponsor)
def sponsorDashboard(request):
    fundrequests = FundRequest.objects.filter(request_confirmed='True', organization=request.organization)[:4]

    return render(request, 'xpro/sponsor/dashboard.html', {'fundrequests': fundrequests})


@user_passes_test(lambda u: u.is_sponsor)
def sponsorProfile(request):

    return render(request, 'xpro/sponsor/profile.html', {'user': request.user})


@transaction.atomic
@user_passes_test(lambda u: u.is_sponsor)
def editSponsorProfile(request):
    if request.method == 'POST':
        user_form = SponsorChangeForm(request.POST, instance=request.user)
        sponsor_form = SponsorProfileForm(request.POST, instance=request.user.sponsor)
        if user_form.is_valid() and sponsor_form.is_valid():
            user_form.save()
            sponsor_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('sponsor-profile')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        user_form = SponsorChangeForm(instance=request.user)
        sponsor_form = SponsorProfileForm(instance=request.user.sponsor)

    return render(request, 'xpro/sponsor/edit_profile.html', {
        'user_form': user_form,
        'sponsor_form': sponsor_form
    })



