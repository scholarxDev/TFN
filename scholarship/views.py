from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Scholarship


# Create your views here.
def search(request):
    if request.method == 'GET':
        form = request.GET.get('q')

        if form is not None:
            lookups = Q(name__icontains=form) | Q(country__icontains=form) | Q(award__icontains=form) | \
                      Q(college__name__icontains=form) | Q(categories__name__icontains=form) 
            results = Scholarship.objects.filter(lookups).distinct()

            context = {
                'results': results,
            }
            return render(request, 'scholarship/search.html', context)

        else:
            return render(request, 'scholarship/search.html')

    return render(request, 'scholarship/search.html')


def scholarship_list(request):
    scholarships_list = Scholarship.objects.filter(organization=request.organization).order_by('-created_on')
    paginator = Paginator(scholarships_list, 100)  # Show 24 contacts per page

    page = request.GET.get('page')
    scholarships = paginator.get_page(page)

    context = {
        "scholarships": scholarships,
    }
    return render(request, "scholarship/index.html", context)


def scholarship_category(request, category):
    scholarships = Scholarship.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "scholarships": scholarships
    }
    return render(request, "scholarship/scholarship_category.html", context)


