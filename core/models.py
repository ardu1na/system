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




class BaseComercial(BaseMain):
    YES = 'YES'
    NO = 'NO'
    DEBATIBLE = 'DEBATIBLE'
    FAIL_CHOICES = (
        (YES, ('YES')),
        (NO, ('NO')),
        (DEBATIBLE, ('DEBATIBLE')),
        )  
    comment_can = models.CharField(max_length=500, blank=True, null=True, verbose_name="COMMENT")
    date_can = models.DateField(null=True, blank=True, verbose_name="DATE")
    fail_can = models.CharField(max_length=50, choices=FAIL_CHOICES, blank=False, default= None, null=True, verbose_name="DO WE FAIL?")  
    cancelled = models.BooleanField(default=False)
    
       
    class Meta:
        abstract = True