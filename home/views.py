from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import posts, Home
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    if request.method == "GET":
        image = request.GET.get('image')
        question = request.GET.get('question')
        home= Home(image= image, question= question)
        home.save()
    return render(request, 'home.html')

def contact(request):
    if request.method == "GET":
        name = request.GET.get('name')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        description = request.GET.get('description')
        contact = Contact(name = name, email = email, phone= phone, description= description, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')

def post(request):
    if request.method == "GET":
        user_name = request.GET.get('user_name')
        title = request.GET.get('title')
        Content = request.GET.get('Content')
        post= posts(user_name = user_name, title = title, Content= Content)
        post.save()

    context = {
        'posts': posts.objects.all()
    }
    return render(request, 'Posts.html',context)