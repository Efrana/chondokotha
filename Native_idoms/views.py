from django.shortcuts import render
from .models import Division, Category, District, Chondokotha
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, "Native_idoms/Home.html")


def data(request):
    context = {
        'division': list(Division.objects.values()),
        'category': list(Category.objects.values()),
    }
    return JsonResponse(context, safe=False)


def district(request):
    print(request.GET)
    print(request.POST)
    queryAll = District.objects
    if request.GET.get('division'):
        queryAll = queryAll.filter(division=request.GET.get('division'))

    district = queryAll.values()
    data = {
            'district': list(district),
        }
    return JsonResponse(data, safe=False)


def chondokotha(request):

    queryAll = Chondokotha.objects

    if request.GET.get('district'):
        queryAll = queryAll.filter(district=request.GET.get('district'))

    if request.GET.get('category'):
        queryAll = queryAll.filter(category=request.GET.get('category'))

    if request.GET.get('division'):
        queryAll = queryAll.filter(district__division=request.GET.get('division'))

    chondokotha = queryAll.values('id','title','district_id','category_id','district__division__id','district__division__name','category__name','district__name')
    data = {
            'chondokotha': list(chondokotha),
        }
    return JsonResponse(data, safe=False)