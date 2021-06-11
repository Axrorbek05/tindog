from django.shortcuts import render
from .models import User, Skills, About, Accomplishments


def index(request):
    user = User.objects.get(id=1)
    user_skills = user.skills.all()
    about = About.objects.get(id=1)
    accomplishments = Accomplishments.objects.all()
    context = {
        'user': user,
        'skills': user_skills,
        'info': about,
        'accomplishments': accomplishments
    }
    return render(request, 'blog/index.html', context)