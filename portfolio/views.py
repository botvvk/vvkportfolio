from typing import TextIO

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def works(request):
    return render(request, 'works.html')

def work(request):
    return render(request, 'work.html')

def contact(request):
    return render(request, 'contact.html')

def write_to_file(params):
    with open('database.txt', mode='a') as database:
        email =params["email"]
        subject =params["subject"]
        message =params["message"]
        file=database.write(f'\n {email}, {subject}, {message}')

def submit(request):
    if request.method=='POST':
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        params={'email': email, 'subject': subject, 'message': message}
        write_to_file(params)
        print(params)

        return render(request, 'thanku.html', params)


