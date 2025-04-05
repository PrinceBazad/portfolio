from django.shortcuts import render
from .models import Profile, Skill, Project, ContactInfo, AboutContent

# Create your views here.

def get_common_context():
    try:
        profile = Profile.objects.first()
        contact_info = ContactInfo.objects.first()
    except (Profile.DoesNotExist, ContactInfo.DoesNotExist):
        profile = None
        contact_info = None
    return {'profile': profile, 'contact_info': contact_info}

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    context = get_common_context()
    return render(request, 'main/contact.html', context)
