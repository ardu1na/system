from django.forms import ModelForm, ModelChoiceField,\
TextInput, URLInput, EmailInput, Select, CheckboxInput
from comercial.models import Sale, Product, Subscription, Adj, Client, SetTier
from django import forms


     
       
    
class AdjForm(ModelForm):
    client = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control wide mb-3',
            'placeholder': 'type client name...',
            'id': 'client',
            'autocomplete': 'on',
            'list': 'clients',
        })
    )
    service = ModelChoiceField(
        queryset=Subscription.objects.filter(state=True),
        widget=Select(
            attrs={
                'class': "default-select form-control wide mb-3",
                'id': "service",
                'placeholder': "service",
            }
        ),
        empty_label=' - ',
        required=False  
    )
    
    class Meta:
        model = Adj
        fields = ['notice_date', 'adj_percent',  'type' ]
        
        widgets = {
            
            'notice_date' : TextInput(attrs={'class':"datetimepicker form-control",
            'id':"PublishDateTimeTextbox",
            'type':"date",
            'placeholder':"Notice Date",}),

      
 
            'adj_percent' : TextInput(attrs={'class':"form-control",
            'id':"adj_percent",
            'placeholder':"Adjustment %",}),

            'type' : Select(attrs={
                'class':"default-select form-control wide mb-3",
                'id':"type",
                'placeholder' : "type",
                'empty_label': "Account/Service"
                }
            ),
        }
        
        
    
class ChangeAdj(AdjForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['type','service', 'client']
        
        
        

class SaleForm(ModelForm):
    
    client = ModelChoiceField(queryset=Client.objects.filter(deleted=False, cancelled=False), widget=Select(attrs={'class':"default-select form-control wide mb-3",
            'id':"client",
            'placeholder':"client",}))

    product = ModelChoiceField(queryset=Product.objects.all(), widget=Select(attrs={'class':"default-select form-control wide mb-3",
            'id':"product",
            'placeholder':"product",}))

    class Meta:
        model = Sale
        
        fields = ['created_at', 'note', 'comments', 'status', 'price']
        
        
        widgets = {
            
            'created_at' : TextInput(attrs={'class':"datetimepicker form-control",
            'id':"PublishDateTimeTextbox",
            'type':"date",
            'placeholder':"Date",}),

            'status' : Select(attrs={'class':"default-select form-control wide mb-3",
            'id':"status",
            'placeholder':"Status $",}),

            'comments' : TextInput(attrs={'class':"form-control",
            'id':"comments",
            'placeholder':"Comments",}),        


            'price' : TextInput(attrs={
                'class':"form-control",
                'id':"price",
                'placeholder' : "Price"
                }
            ),

            'note' : TextInput(attrs={
                'class':"form-control",
                'id':"note",
                'placeholder' : "Notes"
                }
            ),

        }



class ClientSaleForm(SaleForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['client']
    
    
    

class EditSaleForm(SaleForm):        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['created_at']
        

class TierConf(ModelForm):
    class Meta:
        model = SetTier
        fields = '__all__'
        
        widgets = {
            'tier_i' : TextInput(attrs={'class':"form-control",
            'id':"tier_i",
            'placeholder':"Tier I"}),
            
            'tier_ii' : TextInput(attrs={'class':"form-control",
            'id':"tier_ii",
            'placeholder':"Tier II"}),
            
            'tier_iii' : TextInput(attrs={'class':"form-control",
            'id':"tier_iii",
            'placeholder':"Tier III"}),
            
            'tier_iv' : TextInput(attrs={'class':"form-control",
            'id':"tier_iv",
            'placeholder':"Tier IV"}),
            
            
        }



class ClientForm(ModelForm): 
        
    
        
    class Meta:
        model = Client
        
        fields = ['created_at', 'name', 'business_name', 'cuit', 'wop', 'source', 'email', 'tel', 'admin_name', 'admin_email', 'admin_tel', 'website']
        
        
        widgets = {

            'created_at' : TextInput(attrs={'class':"datetimepicker form-control",
            'id':"PublishDateTimeTextbox",
            'type':"date",
            'placeholder':"Date"}),

            'name' : TextInput(attrs={'class':"form-control",
            'id':"name",
            'placeholder':"Client",}),
            
            'business_name' : TextInput(attrs={'class':"form-control",
            'id':"cuit",
            'placeholder':"CUIT",}),

            'website' : URLInput(attrs={'class':"form-control",
            'id':"website",
            'placeholder':"Website",}),

            'cuit' : TextInput(attrs={'class':"form-control",
            'id':"business_name",
            'placeholder':"Business name",}),

            'source' : Select(attrs={
                'class':"default-select form-control wide mb-3",
                'id':"source",
                'placeholder' : "Source",
                }
            ),

            'wop' : Select(attrs={
                'class':"default-select form-control wide mb-3",
                'id':"wop",
                'placeholder':"WOP",}),
            

            'name' : TextInput(attrs={'class':"form-control",
            'id':"name",
            'placeholder':"Full name",}),
            
            'tel' : TextInput(attrs={
                'class':"form-control",
                'id':"tel",
                'placeholder' : "Phone Number"
                }
            ),
            
           
            'email' : EmailInput(attrs={
                'class':"form-control",
                'id':"email",
                'placeholder' : "Email"
                }
            ),
            
            
            
            
            'admin_name' : TextInput(attrs={'class':"form-control",
            'id':"admin_name",
            'placeholder':"Full name",}),
            
            'admin_tel' : TextInput(attrs={
                'class':"form-control",
                'id':"admin_tel",
                'placeholder' : "Phone Number"
                }
            ),
            

            'admin_email' : EmailInput(attrs={
                'class':"form-control",
                'id':"admin_email",
                'placeholder' : "Email"
                }
            ),
            
            
            'admin_email2' : EmailInput(attrs={
                'class':"form-control",
                'id':"admin_email2",
                'placeholder' : "Email 2"
                }
            ),
            
            


        }
        




class EditClientForm(ClientForm):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['created_at']
        
    class Meta:
        fields = ['cancelled', 'date_can' , 'comment_can', 'fail_can']
        
        widgets = {
            'cancelled' : CheckboxInput(attrs={
                'class':"form-control",
            'id':"cancelled",
            'placeholder':"Cancelled?",}),
            
            'date_can' : TextInput(attrs={'class':"datetimepicker form-control",
            'id':"PublishDateTimeTextbox",
            'type':"date",
            'placeholder':"Cancellation date",}),
            
            'fail_can' : Select(attrs={
                'class':"default-select form-control wide mb-3",
            'id':"fail_can",
            'placeholder':"Do we fail?",}),
            
            'comment_can' : TextInput(attrs={
                'class':"form-control",
                'id':"comment_can",
                'placeholder' : "Comment"
                }
            ),
            
        }