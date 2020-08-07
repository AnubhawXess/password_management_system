from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    account_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, help_text='Enter a website or application name (e.g. Github, Desktop)')
    link = models.URLField(blank=True, help_text='(optional) Enter a link to the website (e.g. <a href="http://www.example.com">http://www.example.com</a>)')

    username = models.TextField()
    password = models.TextField()

    def get_absolute_url(self):
        return reverse('account-detail', args=[str(self.id)])
