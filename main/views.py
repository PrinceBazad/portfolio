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
    context = get_common_context()
    try:
        skills = Skill.objects.all()
        projects = Project.objects.all().order_by('-created_at')[:3]  # Get only 3 latest projects
        context['skills'] = skills
        context['projects'] = projects
    except (Skill.DoesNotExist, Project.DoesNotExist):
        context['skills'] = []
        context['projects'] = []
    return render(request, 'main/home.html', context)

def about(request):
    context = get_common_context()
    try:
        about_contents = AboutContent.objects.all()
        context['about_contents'] = about_contents
    except AboutContent.DoesNotExist:
        context['about_contents'] = None
    return render(request, 'main/about.html', context)

def projects(request):
    context = get_common_context()
    try:
        projects = Project.objects.all().order_by('-created_at')
        context['projects'] = projects
    except Project.DoesNotExist:
        context['projects'] = []
    return render(request, 'main/projects.html', context)

def contact(request):
    context = get_common_context()
    return render(request, 'main/contact.html', context)
