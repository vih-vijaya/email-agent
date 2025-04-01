from django.db import models

class SenderRecipient(models.Model):
    sender_email = models.EmailField()
    receiver_email = models.EmailField()

    def __str__(self):
        return f"Sender: {self.sender_email}, Receiver: {self.receiver_email}"
