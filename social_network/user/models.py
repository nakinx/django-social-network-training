from django.db import models

class User(models.Model):        
    username = models.CharField(max_length=128, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=128, null=False)
    
    def __str__(self):
        return "{} {} {}".format(self.username, self.email, self.password)
