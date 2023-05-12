from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager 
from django.contrib.auth.models import Group




class CustomAccountManager(BaseUserManager):
	
	def create_superuser(self, email, username, first_name, last_name, password,**other_fields):
		other_fields.setdefault('is_staff',True)
		other_fields.setdefault('is_superuser',True)
		other_fields.setdefault('is_active',True)
		if other_fields.get('is_staff') is not True:
			raise ValueError(
				'Superuser must be assigned to is_staff=True.')
		if other_fields.get('is_superuser') is not True:
			raise ValueError(
				'Superuser must be assigned to is_superuser=True.')
		super_user = self.create_user(username,email,first_name, last_name, password, **other_fields)
		return super_user

	def create_user(self, username,email, first_name, last_name, password,**other_fields):
		if not email:
			raise ValueError(_('You must provide an email address'))
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, **other_fields)
		user.set_password(password)
		user.save()
		return user


def user_directory_path(instance, filename):
	return f'users/{instance.email}/images/{filename}'

class CustomUser(AbstractBaseUser, PermissionsMixin):
	GENDER_CHOICES = (
		('','Choose gender'),
		('Male', 'Male'),
		('Female', 'Female'),
		('Others', 'Others'),
	)
	username = models.CharField(max_length=191,unique=True)
	email = models.EmailField(_('email address'),unique=True)
	first_name = models.CharField(max_length=255,blank=True)
	last_name = models.CharField(max_length=255,blank=True)
	groups = models.ManyToManyField(Group,blank=True)
	
	is_staff = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	
	objects = CustomAccountManager()

	USERNAME_FIELD = 'email'  
	REQUIRED_FIELDS = ['username','first_name','last_name']
	

	def __str__(self):
		return self.username