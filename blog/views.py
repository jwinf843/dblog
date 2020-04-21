from django.shortcuts import render
# from django.http import HttpResponse # Not using it, don't need it
# Create your views here.

# def home(request):
# 	return HttpResponse('<h1>Blog Home</h1>') # The old way

posts = [
	{
		'author': 'Jordan',
		'title': 'Post 1', 
		'content': 'Post Content 1',
		'date': '20.04.2020',
	},
	{
		'author': 'Jordan',
		'title': 'Post 2', 
		'content': 'Post Content 2',
		'date': '21.04.2020',
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog_templates/home.html', context)

def about(request):
	return render(request, 'blog_templates/about.html')
