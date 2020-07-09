from django.shortcuts import render

# Create your views here.
from .models import Post, Author

def showtitle(request):
    au_name = Author.objects.all()
    contex = {
        'alltitle': au_name
    }
    return render(request, 'title.html', contex)


def postdetails(request,post_name):
    au_name = Author.objects.get(name=post_name)
    alltitle = Post.objects.filter(name = au_name)


    contex = {
        'author': au_name,
        'item': alltitle
    }
    return render(request, 'details/postdetails.html', contex)