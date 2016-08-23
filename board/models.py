from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
	user = models.ForeignKey('auth.User')
	sender_email = models.EmailField()
	title = models.CharField(max_length=200)
	body = models.TextField()
	sent_date = models.DateTimeField(default=timezone.now)
	received_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

