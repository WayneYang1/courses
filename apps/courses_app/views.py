# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
	courses = Course.objects.all()
	context = {
		"courses": courses
	}
	return render(request, 'courses_app/index.html', context)

def courses(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def destroy(request, id):
	course = Course.objects.get(id=id)
	context ={
		"course": course
	}
	return render(request,'courses_app/destroy.html', context)

def no(request):
	return redirect('/')

def yes(request, id):
	course = Course.objects.get(id=id)
	course.delete()
	return redirect('/')
