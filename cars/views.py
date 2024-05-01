from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = (request.GET.get('search'))
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    print(cars)
    
    return render(
        request,
        'cars.html',
        {'cars':cars}
    )