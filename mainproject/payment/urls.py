from django.urls import path
from .views import RazorpayView

urlpatterns = [
    path('razorpay/<int:id>/', RazorpayView.as_view(), name='razorpay'),
]