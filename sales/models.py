from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
from decimal import Decimal

from django.db import models

from customers.models import Client
from core.models import BaseMain, BaseComercial

today = date.today()








class Income(models.Model):
    
    amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    
    sale = models.OneToOneField(
                'Sale', null=True, blank=True, on_delete=models.CASCADE)
    
    subscription = models.ForeignKey(
                'Subscription', related_name="incomes", on_delete=models.CASCADE, null=True, blank=True)
    
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.sale:
            return f"Income ${self.amount} from sale {self.sale}"
        else:
            return f"Monthly income ${self.amount} from subscription {self.subscription}"
        
    class Meta:
        get_latest_by = ['date']
        
        
        
        
        
        
        
        
        
        
        
        

class Product(models.Model):
    name = models.CharField(max_length=50)
    is_rr = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
    
    
class Subscription(BaseComercial):           
        
    service = models.ForeignKey(Product, on_delete=models.CASCADE)
            
    client = models.ForeignKey(Client, related_name="services", on_delete=models.CASCADE)
    
    total = models.DecimalField(default=0, decimal_places=2, max_digits=20)               
    
    def __str__(self):
        
        return f"{self.client} - {self.service}"
    
                
    class Meta:
        unique_together = (('service', 'client'),) 
        get_latest_by = ('created_at')
            
                 
                 
                 
                 
    
    def save(self, *args, **kwargs):
        
        ######################################################################
        ## methods update Income model
        
        # if CREATED
        if not self.pk:            
            is_new_subscription = not self.pk 
            super().save(*args, **kwargs) 
            if is_new_subscription:
                income = Income.objects.create(amount=self.total, subscription=self)
                
                
                 
            

        # monthly create new Income ############################# <----------------------------- how? a view? celery? chanels?
        latest_income = self.incomes.latest('date')
        last_income_date = latest_income.date if latest_income else None
        if last_income_date and today.month != last_income_date.month:
            new_income_date = last_income_date + relativedelta(months=1)
            if today.month > new_income_date.month:
                new_income_date = today.replace(day=1)
            new_income = Income.objects.create(amount=self.total, subscription=self, date=new_income_date)
            
            
            
            
            
        # if  DELETED    
        if self.cancelled or self.deleted:            
            # Find the latest income for the subscription and stop it
            latest_income = self.incomes.latest('date')
            latest_income.subscription = None
            latest_income.save() 

        super().save(*args, **kwargs)       
        
        
        
        
                                         
        """# monthly CREATE INCOME INSTANCE with subscription total , until subscription is cancelled == True           
        if not self.pk:
            # create income
            income = Income.objects.create(amount=self.total, subscription=self) 
        if self.pk and self.cancelled:
            pass # here stop income  
        super(Subscription, self).save(*args, **kwargs) """ 

        
        
                
                
                
                  
class Adj(BaseMain):
    A = "Account"
    S = "Service"
    ADJ_CHOICES = (
        (A, ('Account')),
        (S, ('Service')),
    )
    
    type = models.CharField(max_length=40, default=None, verbose_name="Account/Service", choices=ADJ_CHOICES, blank=False, null=False)
    
    service = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="adj", null=True, blank=True)
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="adj")
       
    adj_percent = models.DecimalField(decimal_places=2, max_digits=16)

    old_value = models.DecimalField(default=0, max_digits=40, decimal_places=2)
    
    new_value = models.DecimalField(default=0, max_digits=40, decimal_places=2)
    
    dif = models.DecimalField(default=0, max_digits=40, decimal_places=2)          
            
    
    def __str__ (self):
        if self.type == "Service":
            client = self.service.client.name
            return f'{self.type}: {self.service} {client} - {self.notice_date}'
        else:
            client = self.client.name
            return f'{self.type}: {client} - {self.notice_date}'
        
    class Meta:
        ordering = ['-notice_date']
        verbose_name = "Adjustment"       
        verbose_name_plural = "Adjustments"

        

    notice_date = models.DateField(null=True,blank=True)
    done = models.BooleanField(default=False)

    email_date = models.DateField(null=True, blank=True)
    
    remind_sent = models.BooleanField(default=False)
    
   
    def save(self, *args, **kwargs):
        if self.notice_date:
            fifteen_days_before = self.notice_date - timedelta(days=15)
            self.email_date =   fifteen_days_before
        
        super(Adj, self).save(*args, **kwargs)
                    










class Sale(BaseMain):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="sales", null=True, blank=True)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales", null=True, blank=True)
    
    subscription = models.ForeignKey(Subscription, related_name="sales", on_delete=models.CASCADE, null=True, blank=True, editable=False)      
                   
    def __str__(self):
       return '{} - {} '.format(self.client, self.product)
     
       
    class Meta:
        ordering = ['-created_at']        
   
    kind = models.CharField(max_length=50, null=True, blank=True, verbose_name="KIND")
    
    note = models.CharField(max_length=400, null=True, blank=True, verbose_name="NOTES")
    
    comments =models.CharField(max_length=500, null=True, blank=True, verbose_name="COMMENTS")
        
    P = "P"
    FCD = "FCD"
    FC = "FC"
    STATUS_CHOICES=(
        (P, ("P")),
        (FCD, ("FCD")),
        (FC, ("FC")),)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, null=True, blank=False, default=None, verbose_name="STATUS $") 
      
    price = models.DecimalField(default=0, verbose_name="PRICE", decimal_places=2, max_digits=12)         

      
      
      
      
      
      
      
      
      
    
    ################### 
    def create_subscription_or_update (self, *args, **kwargs):
        if self.product.is_rr:  
            try:
                subscription = Subscription.objects.get(
                    client=self.client, service=self.product) 
                                
                subscription.total += Decimal(self.price)
                subscription.save()     
                self.subscription=subscription  
                            
            except Subscription.DoesNotExist:  
                values = {
                    "client": self.client,
                    "service": self.product,
                    "total": self.price,                }            
                subscription = Subscription(**values)
                subscription.save()  
                self.subscription=subscription            
            
            
    def save(self, *args, **kwargs):                                    

        if self.pk:
            
            
            if self.subscription:   
                old_total = self.price
                self.subscription.total -= old_total
                self.subscription.save()
                
                super().save(*args, **kwargs)
                
                self.subscription.total += self.price
                self.subscription.save()
                    
            
            if self.deleted and self.subscription:
                self.subscription.total -= self.price
                self.subscription.save()
                self.subscription = None
                
            super(Sale, self).save(*args, **kwargs)

             
        else:
             # get kind       
            client_sales = Sale.objects.filter(client=self.client)
            same_product = client_sales.filter(product=self.product)
            
            if not client_sales.exists():
                self.kind = "New Client"
            elif same_product.exists():
                self.kind = "Up Sell"
            else:
                self.kind = "Cross Sell"
                
                
            if self.product.is_rr and self.subscription is None:
                self.create_subscription_or_update()
            
        
            super(Sale, self).save(*args, **kwargs)  
            
            if self.product.is_rr == False:
                income = Income.objects.create(amount=self.price, sale=self)
            
    
        
    def delete(self, *args, **kwargs):
    # update asociated subscription values           
        subscription = self.subscription
        subscription.total -= self.price
        subscription.save()
        super().delete(*args, **kwargs)    
        
              
            