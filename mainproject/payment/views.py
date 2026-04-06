import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from learning.models import Course
from django.utils import timezone
from django.db import transaction
from payment.models import Transactions

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
    
class PaymentVerifyView(View):

    def post(self,request,*args,**kwargs):

        rzp_order_id=request.POST.get('razorpay_order_id')

        rzp_payment_id=request.POST.get('razorpay_payment_id')
        
        rzp_payment_signature=request.POST.get('razorpay_signature')

        transaction_obj=Transactions.objects.get(rzp_order_id=rzp_order_id)

        transaction_obj.rzp_payment_id=rzp_payment_id

        transaction_obj.rzp_signature=rzp_payment_signature

        transaction_obj.save()

        client = razorpay.Client(auth=(config("RZP_CLIENT_ID"), config("RZP_CLIENT_SECRET")))

        paid=client.utility.verify_payment_signature({
                                                'razorpay_order_id': rzp_order_id,
                                                'razorpay_payment_id': rzp_payment_id,
                                                'razorpay_signature': rzp_payment_signature
                                                })
        
        if paid:

            transaction_obj.status='Success'

            transaction_obj.save()

            user_subscription=transaction_obj.user_subscription

            start_date=timezone.now()

            end_date=start_date+timezone.timedelta(days=30)

            user_subscription.start_date=timezone.now()

            user_subscription.end_date=timezone.timedelta(days=30)

            user_subscription.start_date=start_date

            user_subscription.end_date=end_date

            user_subscription.active=True

            user_subscription.save()

            return redirect('home')
        
        transaction_obj.status='Failed'

        transaction_obj.save()

        return redirect('razorpay',uuid=user_subscription.plan.uuid)
    