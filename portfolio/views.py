from django.shortcuts import render
from .models import Project
from .models import PhotoResume
# Create your views here.
def home(request):
    projects=Project.objects.all()
    files=PhotoResume.objects.all()
    return render(request, 'portfolio/main.html',{'projects':projects, 'files':files})


