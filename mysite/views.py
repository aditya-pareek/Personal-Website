from django.shortcuts import render
import requests, json
from . models import Contact

def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
    else:
        firstname = 'Aditya'
        lastname = 'Pareek'

    r = requests.get('http://api.icndb.com/jokes/random?firstName='+ firstname +'&lastName= '+ lastname +'')
    json_data = json.loads(r.text)
    joke = json_data.get('value').get('joke')
        
    context = {'j': joke}
    return render(request, 'mysite/index.html', context)

def portfolio(request):
    return render(request, 'mysite/portfolio.html')

def contact(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        s = request.POST.get('subject')
        m = request.POST.get('message')

        c = Contact(email=e, subject=s, message=m)
        c.save()

        return render(request, 'mysite/thanks.html')
    else:
        return render(request, 'mysite/contact.html')