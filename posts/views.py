from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Posts

# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM HOST')

    posts = Posts.objects.all()

    context = {
        'title' : 'Latest Posts',
        'posts' : posts,
    }

    return render(request,'posts/index.html',context)

def detail(request,id):
    post= Posts.objects.get(id=id)

    context = {
        'post' : post,
    }

    return render(request,'posts/details.html',context)

def add(request):
    return render(request,'posts/addnew.html')

def insert(request):
    if request.POST:

        #return HttpResponse('HELLO FROM POST request')
        data = request.POST.copy()
        title = data.get('blogtitle')
        body = data.get('blogbody')
        post=Posts.objects.create(title=title ,body=body)
        post.save()
        messages.success(request, 'New blog inserted successfully')
        return redirect('/index')

def delete(request,id):
    Posts.objects.filter(id=id).delete()
    messages.success(request, 'Requested blog deleted successfully')
    return redirect('/index')

def update(request,id):
    if request.POST:
        post = Posts.objects.get(id=id)
        data = request.POST.copy()
        post.title = data.get('blogtitle')
        post.body = data.get('blogbody')
        post.save()
        messages.success(request, 'New blog updated successfully')
        return redirect('/index')

    else:

        post= Posts.objects.get(id=id)

        context = {
            'post' : post,
        }
        return render(request,'posts/update.html',context)

def notfound(request):
    return render(request, 'posts/404.html')