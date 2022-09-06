import json
from django.shortcuts import render, HttpResponse
from .models import Newsletter


# Create your views here.
def newsletter(request):
    if request.method == "POST":
        email = request.POST['email']

        # create a new newsletter subscription object.
        new_subscription = Newsletter(email=email)
        new_subscription.save()

        resp = json.dumps({"response": "subscribed"})
        return HttpResponse(resp)

    else:
        resp = json.dumps({"response": "error"})
        return HttpResponse(resp)


def subscribed(request):

    return render(request, 'newsletter/subscribed.html', {})
