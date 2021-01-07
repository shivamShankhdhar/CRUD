from django.db import models

# Create your models here.
class Task(models.Model):
	name 		= models.CharField(max_length = 200)
	is_active 	= models.BooleanField(default= True)
	timestamp 	= models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.name

