from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
# 	return HttpResponse('<h1>Blog Home</h1>') # The old way

def home(request):
	return render(request, 'blog_templates/home.html')

def about(request):
	return render(request, 'blog_templates/about.html')
