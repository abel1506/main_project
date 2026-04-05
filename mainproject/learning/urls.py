from django.urls import path
from .views import HomeView, AboutView, CourseListView, ContactView
from django.contrib.auth.views import LoginView, LogoutView
from .views import CourseDetailView




urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_details'),


]
