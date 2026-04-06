import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views import View
from learning.models import Course

from decouple import config

from .models import Payment

class RazorpayView(View):

    template = 'learning/razorpay.html'

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        course = get_object_or_404(Course, id=id)

        payment, _ = Payment.objects.get_or_create(course=course, user=request.user, amount=course.price)


        client = razorpay.Client(auth=(config('RZP_KEY_ID'), config('RZP_KEY_SECRET')))

        data = { "amount": payment.amount*100, "currency": "INR", "receipt": "order_rcptid_11" }

        rzp_payment = client.order.create(data=data) 

        rzp_order_id = rzp_payment.get('id')

        data = {'RZP_KEY_ID':config('RZP_KEY_ID'),'amount':rzp_payment.get('amount'),'rzp_order_id':rzp_order_id}

        return render(request,self.template,context=data)
    