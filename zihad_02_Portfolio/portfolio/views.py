from django.shortcuts import render, get_object_or_404
from .models import Hero, About, Skill, Project, Experience, Education, Contact, BlogPost, BlogCategory
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    hero = Hero.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()[:6]  # Show latest 6 projects
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    context = {
        'hero': hero,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    about = About.objects.first()
    return render(request, 'portfolio/about.html', {'about': about})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experience.html', {'experiences': experiences})

def education(request):
    educations = Education.objects.all()
    return render(request, 'portfolio/education.html', {'educations': educations})

def blog(request):
    posts = BlogPost.objects.all()
    categories = BlogCategory.objects.all()
    return render(request, 'portfolio/blog.html', {'posts': posts, 'categories': categories})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return JsonResponse({'success': True})
    return render(request, 'portfolio/contact.html')
