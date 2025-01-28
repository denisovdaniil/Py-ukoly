from django.http import HttpResponse 
from django.shortcuts import render
import random
import datetime as dt


# Create your views here.

"""
'' -> index_page

"""
def index_page(request):

    print(request.method)
    print(request.path)
    number = random.randint(1, 100)
    d = dt.datetime.now()

    return HttpResponse(f'<h1>Hello From Django: {number} | {d}</h1><img src="https://picsum.photos/200/300">')

def url_paths(request):

    print(request.GET)
    print(request.GET['XYZ'])
    print(request.GET.getlist('XYZ'))
    # ?key=value&XYZ=10&XYZ=20

    return HttpResponse('This page is working')

def time_page(request):

    d = dt.datetime.now()
    dd = d.strftime("%d. %m. %Y")
    ddd = d.strftime("%H:%M:%S")

    return HttpResponse(f'<h1>Today is {dd} <br> {ddd}</h1>')

def my_math(request):

    """
    ?operation=plus&a=10&b=100
    operation=plus | minus | multiply | divide
    a=první číslo
    b=druhé číslo
    """

    a = int(request.GET['a'])
    b = int(request.GET['b'])
    operation = request.GET['operation']

    if operation == 'plus':
        result = a + b
    elif operation == 'minus':
        result = a - b
 


    return HttpResponse(f'RESULT: {result}')

# MVC - model view controller (ovladač)
# MVT - model view (pohled) template (HTML šablona)

def test_template(request):

    print(request.GET)
    name = request.GET.get('name', 'World')
    age = int(request.GET.get('age', 0))

   
    """
    try:
        name = request.GET['name']
    except KeyError:
        name = 'World'

    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = 'World'
    """
    context = {

        'date': dt.datetime.now(),
        'name': name,
        'age': age,
    }
    # render = vykreslit
    return render(request, 'test_template.html', context)

def calculator(request):
    try:

        a = int(request.GET['a'])
        b = int(request.GET['b'])
        result = a + b 
    except (KeyError, TypeError, ValueError):
        result = ''

    context = {
        'result': result
    }
    return render(request, 'calculator.html', context)

def age(request):
    try:

        year = int(request.GET['year'])
        
        result = 2025 - year 
    except (KeyError, TypeError, ValueError):
        result = ''

    context = {
        'result': result
    }

    return render(request, 'age.html', context)

