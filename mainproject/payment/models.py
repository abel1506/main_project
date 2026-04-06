from django.conf import settings
from django.db import models

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