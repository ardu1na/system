from datetime import date

from django.db import models

today = date.today
 
class BaseMain(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(editable=False, null=True, blank=True)    
    deleted = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.deleted:
            self.deleted_at = today
        super().save(*args, **kwargs)
        
    class Meta:
        abstract = True



