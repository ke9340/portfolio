from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Education, Experience, Skill, Achievement, Feedback  # Added Feedback model
from .forms import FeedbackForm
from django.http import JsonResponse


def contact(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Thank you for your feedback!"})
        else:
            return JsonResponse({"success": False, "message": "Please fill all fields correctly!"})

    return render(request, 'home.html', {'form': FeedbackForm()})

def home(request):
    projects = Project.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    achievement = Achievement.objects.all()

    categorized_skills = {}
    for skill in skills:
        categorized_skills.setdefault(skill.category, []).append(skill.name)

    return render(request, 'home.html', {
        'projects': projects,
        'education': education,
        'experience': experience,
        'skills': categorized_skills,
        'achievements': achievement
    })
