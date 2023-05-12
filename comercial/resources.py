from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from comercial.models import Sale, Adj, Subscription, Income, Product, Client

   
   
class SaleResource(resources.ModelResource):
    client = fields.Field(
        column_name='client',
        attribute='client',
        widget=ForeignKeyWidget(Client, 'name')
    )
    
    class Meta:
        model = Sale
        
        

class AdjResource(resources.ModelResource):
    client = fields.Field(
        column_name='client',
        attribute='client',
        widget=ForeignKeyWidget(Client, 'name')
    )
    
    service = fields.Field(
        column_name='service',
        attribute='service',
        
        widget=ForeignKeyWidget(Subscription, 'service')
    )
    
    class Meta:
        model = Adj
        





class SubResource(resources.ModelResource):
    client = fields.Field(
        column_name='client',
        attribute='client',
        widget=ForeignKeyWidget(Client, 'name')
    )
    
    service = fields.Field(
        column_name='service',
        attribute='service',
        
        widget=ForeignKeyWidget(Product, 'name')
    )
    
    class Meta:
        model = Subscription
        
        



class IncomeResource(resources.ModelResource):
    subscription = fields.Field(
        column_name='subscription',
        attribute='subscription',
        widget=ForeignKeyWidget(Subscription, 'service')
    )
    
    sale = fields.Field(
        column_name='sale',
        attribute='sale',
        
        widget=ForeignKeyWidget(Sale, 'product')
    )
    
    class Meta:
        model = Income
        


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        
        

class ClientResource(resources.ModelResource):
    class Meta:
        model = Client