from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import *


def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {'page_obj': page_obj})


@login_required(login_url='/login')
def new_post(request):
    
    form = PostForms()

    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        form.author = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'posts/newpost.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    text = post.content.split('\r\n')
    context = {
        'post': post,
        'text': text
    }


    return render(request, 'posts/post-detail.html', context)

def register(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)          
            return redirect('/')  
    
    context = {
        
    }

    return render(request, 'posts/register.html', context)

def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/profile')


    return render(request, 'posts/login.html')

def userlogout(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def profile(request):
    return render(request, 'posts/profile.html',)

@login_required(login_url='/login')
def update_profile(request):

    if request.method == 'POST':
        user = Image.objects.get(user=request.user)
        form = UpdateUser(request.POST, request.FILES, instance = user)
        if form.is_valid():
            inst = form.save()
            inst.save()
            return redirect('/profile')

    return render(request, 'posts/update.html',)