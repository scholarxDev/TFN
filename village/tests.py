from django.test import TestCase
from django.db.models import Sum

# Create your tests here.
def request_list(request):
	village = Village.objects.all()
	
	fundrequests = FundRequest.objects.filter(request_confirmed='True', complete='False')
	for fundrequest in fundrequests:
		if fundrequest.percentage_raised >= 99:
			village.fund_request_count = +FundRequest.objects.count()
			village.fully_funded = +FundRequest.objects.filter(complete='True').count()
			village.total_amount_raised = +FundRequest.objects.aggregate(Sum('amount_raised'))['amount_raised__sum']
			fundrequest.complete = True
			fundrequest.save()
	
	return render(request, 'village/index.html', {
		'village': village,
		'fundrequests': fundrequests
	})


# Create your views here.
def request_list(request):
	village = Village.objects.all()
	village.fund_request_count = +FundRequest.objects.count()
	village.fully_funded = +FundRequest.objects.filter(complete='True').count()
	village.total_amount_raised = +FundRequest.objects.aggregate(Sum('amount_raised'))['amount_raised__sum']
	

	fundrequests = FundRequest.objects.filter(request_confirmed='True', complete='False')
	for fundrequest in fundrequests:
		if fundrequest.percentage_raised >= 99:
			fundrequest.complete = True
			fundrequest.save()
	
	return render(request, 'village/index.html', {
		'village': village,
		'fundrequests': fundrequests
	})

