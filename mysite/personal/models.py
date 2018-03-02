from __future__ import unicode_literals

from django.db import models

class contactForm(models.Model):
 name=models.CharField(max_length=140)
 email=models.TextField()
 message=models.TextField()
 
 
def __unicode__(self):
   return self.name
   return self.email
 