from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from django.db import transaction
from .forms import FundRequestForm, TfnFundRequestForm
from .models import FundRequest, Village
from payment.models import Payment
from django.db.models import Sum


# Create your views here.
def request_list(request):
	village = Village.objects.filter(organization=request.organization)

	village.fund_request_count = +FundRequest.objects.filter(organization=request.organization).count()
	village.fully_funded = +FundRequest.objects.filter(complete='True', organization=request.organization).count()
	village.total_amount_raised = +FundRequest.objects.aggregate(Sum('amount_raised'))['amount_raised__sum']
	

	fundrequests = FundRequest.objects.filter(request_confirmed='True', complete='False', organization=request.organization)
	for fundrequest in fundrequests:
		if fundrequest.percentage_raised >= 99:
			fundrequest.complete = True
			fundrequest.save()
	
	return render(request, 'village/index.html', {
		'village': village,
		'fundrequests': fundrequests,
		'total_raised': village.total_amount_raised,
		'fully_funded': village.filter(fully_funded=True).count()
	})


@login_required
@user_passes_test(lambda u: u.is_student or u.is_school)
@transaction.atomic
def fundrequest(request):
	use_form = FundRequestForm if request.organization.name == "scholarx" else TfnFundRequestForm
	if request.method == 'POST':
		form = use_form(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.organization = request.organization
			instance.save()
			return redirect('request_submitted')

	else:
		form = use_form()
	
	return render(request, 'village/fundrequest.html', {'form': form})


def request_submitted(request):
	
	return render(request, 'village/request_submitted.html', {})


@transaction.atomic
def request_detail(request, pk):
	fundrequest = FundRequest.objects.get(pk=pk)
	payment = Payment.objects.filter(meta_data=fundrequest.id)
	donations = []

	for payments in payment:
		donations.append(payments.amount)
		fundrequest.amount_raised = sum(donations)
		fundrequest.percentage_raised = int((fundrequest.amount_raised/int(fundrequest.How_much_do_you_need))*100)
		fundrequest.save()

	context = {
		'fundrequest': fundrequest,
		'payment': payment,
	}
	
	return render(request, 'village/request_detail.html', context)
