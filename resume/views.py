from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'resume/home.html')

def contact(request):
    return render(request, 'resume/contact.html')

def education(request):
    return render(request, 'resume/education.html')

def relevent_course(request):
    return render(request, 'resume/relevent course.html')

def skills(request):
    return render(request, 'resume/skills.html')

def thankyou(request):
    return render(request, 'resume/thankyou.html')

def work_experience(request):
    return render(request, 'resume/work experience.html')