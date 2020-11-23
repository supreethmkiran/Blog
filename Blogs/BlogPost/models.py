from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):
	author = models.CharField(max_length =200)
	title = models.CharField(max_length =200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def str(self):
		return self.title

class user_details(models.Model):
    username = models.CharField(max_length=200,primary_key="true")
    first_name = models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    passw=models.CharField(max_length=200)
    cpass=models.CharField(max_length=200)
    insta=models.TextField()
    fb=models.TextField()
