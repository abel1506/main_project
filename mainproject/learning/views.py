from django.views import View
from django.shortcuts import render
from .models import Course
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Course
import razorpay
from django.conf import settings


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")

class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "courses/about.html")

class CourseListView(View):
    def get(self, request, *args, **kwargs):
        course = Course.objects.all()
        return render(request, "learning/course_list.html")

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")


class CourseDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, pk=pk)

        context = {
            "course": course
        }

        return render(request, "course_detail.html", context)
    
class PaymentView(View):

    def get(self, request, pk, *args, **kwargs):
        course = Course.objects.get(id=pk)

        client = razorpay.Client(auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        ))

        payment = client.order.create({
            "amount": int(course.price * 100),
            "currency": "INR",
            "payment_capture": "1"
        })

        context = {
            "course": course,
            "payment": payment,
            "key": settings.RAZORPAY_KEY_ID
        }

        return render(request, "payment.html", context)