from django.conf import settings
from django.db import models
from learning.models import BaseClass

class Payment(models.Model):
    course = models.ForeignKey('learning.Course', on_delete=models.CASCADE)
    
   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    order_id = models.CharField(max_length=200)
    payment_id = models.CharField(max_length=200, null=True, blank=True)
    signature = models.CharField(max_length=500, null=True, blank=True)
    amount = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.course.title
class PaymentStatusChoice(models.TextChoices):

    PENDING = 'Pending','Pending'

    SUCCESS = 'Success','Success'

    FAILED = 'Failed','Failed'
class Transactions(BaseClass):

    payment = models.ForeignKey('Payment',on_delete=models.CASCADE)

    rzp_order_id = models.SlugField()

    amount = models.FloatField()

    status = models.CharField(max_length=20,choices=PaymentStatusChoice.choices,default=PaymentStatusChoice.PENDING)

    transaction_at = models.DateTimeField(null=True,blank=True)

    rzp_payment_id = models.SlugField(null = True,blank=True)

    rzp_signature = models.TextField()

    def __str__(self):

        return f'{self.payment.learning.profile.first_name}-{self.payment.learning.name}-transaction-{self.created_at}'

    class Meta:

        verbose_name = 'Transactions'

        verbose_name_plural = 'Transactions'
