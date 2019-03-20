from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime,timedelta
from userauth.models import Users

from .models import Posts,Comments

# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM HOST')
    if request.session.has_key('username'):
        username = request.session['username']
        posts = Posts.objects.all()
        username = request.session['username']

        context = {
            'title' : 'Posts',
            'posts' : posts,
            'username': username,
        }

        return render(request,'posts/index.html',context)

    else:
        return redirect('../user/login')

def detail(request,id):
    post = Posts.objects.get(id=id)
    comment = reversed(Comments.objects.filter(post_id=post.id))
    if request.session.has_key('username'):
        username = request.session['username']
    #com = Comments.objects.select_related('user').filter(post_id=post.id)

    context = {
        'post' : post,
        'comment': comment,
        'username': username,
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
        st=datetime.now()+timedelta(hours=-4)
        #dt = datetime.now().astimezone(pytz.timezone("America/Toronto"))

        if title.replace(" ","").isalpha() and body.replace(" ","").isalpha():

            if request.session.has_key('username'):
                username = request.session['username']
                user = Users.objects.all()
                for u in user:
                    if u.email_id==username:
                        userid=u.id
            post=Posts.objects.create(title=title ,body=body, posted_on=st,user_id=userid)
            post.save()
            messages.success(request, 'New blog inserted successfully')
            return redirect('/index')

        else:
            messages.error(request, 'Title or body must be not empty')
            return redirect('./addnew')

def delete(request,id):
    Posts.objects.filter(id=id).delete()
    messages.success(request, 'Requested blog deleted successfully')
    return redirect('/index')

def update(request,id):
    if request.POST:
        post = Posts.objects.get(id=id)
        data = request.POST.copy()

        if data.get('blogtitle').replace(" ","").isalpha() and data.get('blogbody').replace(" ","").isalpha():

            post.title = data.get('blogtitle')
            post.body = data.get('blogbody')
            post.save()
            messages.success(request, 'Requested blog updated successfully')
            return redirect('/index')

        else:
            messages.error(request, 'Title or body must be not empty')
            return redirect('./'+id)

    else:
        post= Posts.objects.get(id=id)

        context = {
            'post' : post,
        }
        return render(request,'posts/update.html',context)

def notfound(request):
    return render(request, 'posts/404.html')

def postcomment(request):
    data = request.POST.copy()
    comment = data.get('comment')

    if comment.replace(" ","").isalpha():

        st=datetime.now()+timedelta(hours=-4)
        postid = data.get('id')
        if request.session.has_key('username'):
            username = request.session['username']
            user = Users.objects.all()
            for u in user:
                if u.email_id == username:
                    userid = u.id
        comment = Comments.objects.create(comment=comment, posted_on=st, user_id=userid, post_id=postid)
        comment.save()

        return redirect('./'+postid)

    else:
        messages.error(request, 'comment must be not empty')
        return redirect('./' + data.get('id'))