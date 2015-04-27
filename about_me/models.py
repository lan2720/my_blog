from django.db import models

# Create your models here.
class About(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True)    

    def __unicode__(self):
        return unicode(self.id) 
    
    class Meta:
        ordering = ('-created_time',)
