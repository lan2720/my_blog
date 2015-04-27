from django.shortcuts import render,get_object_or_404
from about_me.models import About

# Create your views here.
def about(request):
    about_text = About.objects.all()[0]
    return render(request, 'about_me/about.html', {'about': about_text})
