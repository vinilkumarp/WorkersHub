from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    first_name = models.CharField(max_length=100, default='')
    description= models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.CharField(max_length=12,default='')


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



class Category(models.Model):
	CHOICES=(
		('Plumber','Plumber'),
		('Carpenter','Carpenter'),
		('Electrician','Electrician'),
		('Gardener','Gardener'),
		)

	cat=models.CharField(max_length=20,choices=CHOICES)
	
	def __str__(self):
		return self.cat
	def get_absolute_url(self):
		return reverse('identity', kwargs={'pk': self.pk})
	
	
	
class WorkerProfile(models.Model):

	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=50, default='')
	#Jobtitle = models.CharField(max_length=50, default='')
	phone_number = models.CharField(max_length=12,default='')
	busy=models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('send_conf',kwargs={'id': self.id})
