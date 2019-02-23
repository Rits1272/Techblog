from .forms import CustomUserForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from .models import Ask
from django.utils import timezone
from basic_app.forms import PostForm

def register(request):
	if request.method == 'POST':
		f = CustomUserForm(request.POST)

		if f.is_valid():
			f.save()
			messages.success(request,"User registered successfully!")
			return redirect(register)

	else:
		f = CustomUserForm()
		
	return render(request, 'basic_app/regis.html', {'form' : f})

def index(request):
	return render(request, 'basic_app/base.html', {})

def login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(request,user)
			return redirect('index')

		else:
			messages.error(request, "Incorrect Username or password")

	return render(request, 'basic_app/login.html', {})

def logout(request):
	auth.logout(request)
	return render(request, 'basic_app/logout.html', {})

def questions_list(request):
	ques = Ask.objects.filter(created_date__lte = timezone.now()).order_by('-created_date')
	return render(request, 'basic_app/qlist.html', {'ques' : ques})

def post(request):

	if request.method == 'POST':
		post = PostForm(request.POST)

		if post.is_valid():
			form = post.save(commit = False)
			form.author = request.user
			form.created_date = timezone.now()
			form.save()
			return redirect('ques')

	else:
		post = PostForm()
		

	return render(request,'basic_app/post_new.html', {'post' : post})



