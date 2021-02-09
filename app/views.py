from django.shortcuts import render, HttpResponse
from datetime import datetime
from app.models import (Contact, About, Fact, Skill, Summary, 
Education, Professional, Application, Startup, Web, Service, SocialMedia, Profile)
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()

        # Send mail
        send_mail(
            subject,
            message=f"Name: {name} \nEmail: {email} \n{message}: ",
            from_email=email,
            recipient_list= ['example@email.com'],
            fail_silently=False,
        )
           
        messages.success(request, 'Your message has been sent.')
        
    context = {
        "about": About.objects.first(),
        "fact": Fact.objects.all(),
        "skill": Skill.objects.all(),
        "summary": Summary.objects.first(),
        "education": Education.objects.all(),
        "professional": Professional.objects.all(),
        "application": Application.objects.all(),
        "startup": Startup.objects.all(),
        "web": Web.objects.all(),
        "service": Service.objects.all(),
        "social": SocialMedia.objects.first(),
        "profile": Profile.objects.first()
    }
    return render(request, "index.html", context)

def apps(request, slug):
    context = {
        "application": Application.objects.filter(slug=slug).first(),
        "social": SocialMedia.objects.first(),
        "profile": Profile.objects.first()
    }
    return render(request, "apps.html", context)

def web(request, slug):
    context = {
        "web": Web.objects.filter(slug=slug).first(),
        "social": SocialMedia.objects.first(),
        "profile": Profile.objects.first()
    }
    return render(request, "web.html", context)

def startup(request, slug):
    context = {
        "startup": Startup.objects.filter(slug=slug).first(),
        "social": SocialMedia.objects.first(),
        "profile": Profile.objects.first()
    }
    return render(request, "startup.html", context)