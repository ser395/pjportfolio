from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    #return HttpResponse("My personal Portfolio")
    return render(request,'core/index.html',{})
# def about(request):
#     return HttpResponse(('Acerca de mi....Soy desarrollador web y programador'))
def about(request):
    return render(request, 'core/about.html')
# def portfolio(request):
#     return HttpResponse('Estos son mis trabajos mas recientes')
def portfolio(request):
    return render(request,'core/portfolio.html',{})

# def contact(request):
#     return HttpResponse('Para comunicarse llamar al telefono: +54 11 30302124')

def contact(request):
    return render(request,'core/contact.html',{})
