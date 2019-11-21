
from django.core.signals import request_started
from django.dispatch import receiver
from authenticate.views import register

@receiver(request_started,sender=register)
def func(sender,**kwargs):
    print("request finnished")
    