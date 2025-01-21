from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
# Create your views here.

def index(request): 
    context = {
        'title': 'Home Page',
        'content': 'Welcome to Home Page'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home page")
def about(request): 
    return render(request, 'about.html')
def services(request): 
    return render(request, 'services.html')
def contact(request): 
    if request.method == 'POST': 
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phone = request.POST.get('phone')
        contact = Contact(name=name, email=email, desc=desc, phone=phone,date = datetime.today())
        contact.save()
    return render(request, 'contact.html')