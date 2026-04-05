from django.urls import path
from .views import HomeView, AboutView, CourseListView, ContactView, CourseDetailView, PaymentView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path('courses/', CourseListView.as_view(), name='courses'),
    
    # ✅ FIXED name
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    
    # ✅ FIXED import (no views.)
    path('payment/<int:pk>/', PaymentView.as_view(), name='payment'),
]