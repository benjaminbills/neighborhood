from customer.filters import BusinessFilter
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib import messages
from .forms import  BusinessForm, CreateUserForm, PostForm, ProfileForm
from .models import Business, Post, Profile


# Create your views here.
def home(request):
    businesses = Business.objects.all()
    posts = Post.objects.all()
    context = {'posts':posts,'businesses':businesses }
    return render(request, 'home.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'registration/login.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Profile.objects.create(
                user=user,
            )
            # send_welcome_email(user.username,user.email)
            messages.success(request, 'Account was creates for ' + username )
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request, user_id):
    profile = Profile.objects.get(user=user_id)
    
    context = {'profile':profile}
    return render(request, 'profile/profile.html', context)

@login_required(login_url='login')
def accountSettings(request):
	profile = request.user.profile
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profile/profile_edit.html', context)

@login_required(login_url='login')
def addBusiness(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('home')

    else:
        form = BusinessForm()
    context = {'form':form}
    return render(request, 'business/business_add.html', context)

def getBusinesses(request):
    businesses = Business.objects.all()
    
    context = {'businesses':businesses }
    return render(request, 'business/businesses.html', context)

@login_required(login_url='login')
def getBusiness(request, business_id):
    current_user = request.user
    business = Business.objects.get(pk=business_id)
    context = {'business':business}
    return render(request, 'business/business.html', context)

@login_required(login_url='login')
def addPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('get_posts')

    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'post/post_add.html', context)

def getPosts(request):
    posts = Post.objects.all()
    
    context = {'posts':posts }
    return render(request, 'post/posts.html', context)

@login_required(login_url='login')
def getPost(request, post_id):
    current_user = request.user
    post = Post.objects.get(pk=post_id)
    context = {'post':post}
    return render(request, 'post/post.html', context)

def search(request):
    businesses = Business.objects.all()
    myFilter = BusinessFilter(request.GET, queryset=businesses)
    businesses = myFilter.qs
    context = {'businesses':businesses, 'myFilter':myFilter}
    return render(request, 'business/search.html', context)