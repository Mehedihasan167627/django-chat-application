from django.db import models
from accounts.models import CustomUser
from django.db.models import Q 
# Create your models here.
class Chat(models.Model):
    sender=models.ForeignKey(CustomUser,related_name="sender",on_delete=models.CASCADE)
    message=models.CharField(max_length=255)
    receiver=models.ForeignKey(CustomUser,related_name="receiver",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.message

    
    @staticmethod
    def get_messages(sender,receiver):
        return Chat.objects.filter(
            Q(sender=sender,receiver=receiver) |
            Q(sender=receiver,receiver=sender)
        ).order_by("id")
    


