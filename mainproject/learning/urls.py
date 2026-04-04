from django.urls import path
from .views import HomeView, AboutView, CourseListView, ContactView
from django.contrib.auth.views import LoginView, LogoutView
from .views import CourseDetailView
from .views import PaymentView



urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("courses/", CourseListView.as_view(), name="courses"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("payment/<int:pk>/", PaymentView.as_view(), name="payment"),
]
