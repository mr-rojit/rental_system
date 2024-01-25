from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="frm")
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to")

    def __str__(self):
        return self.message

