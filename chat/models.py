from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Channel(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_one')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_two')

    def __str__(self):
        return 'A challenl'


class Chat(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="frm")
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

