from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from .models import Course



class HomeView(View):
    template = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template)


class AboutView(View):
    template = "courses/about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template)


class CourseListView(View):
    template = "learning/course_list.html"

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()

        context = {
            "courses": courses
        }

        return render(request, self.template, context)


class CourseDetailView(View):
    template = "learning/course_details.html"

    def get(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, pk=pk)

        context = {
            "course": course
        }

        return render(request, self.template, context)


class ContactView(View):
    template = "contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template)
    

