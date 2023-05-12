"""from django.forms import ModelForm, \
TextInput, URLInput, EmailInput, Select, Textarea
from clients.models import Client,  SetTier

        

class TierConf(ModelForm):
    class Meta:
        model = SetTier
        exclude = ['id', 'tier_v']
        
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
        
        exclude = ['id', 'cancelled', 'comment_can', 'date_can', 'fail_can']
        
        
        widgets = {

            'date' : TextInput(attrs={'class':"datetimepicker form-control",
            'id':"PublishDateTimeTextbox",
            'type':"date",
            'placeholder':"Date"}),

            'name' : TextInput(attrs={'class':"form-control",
            'id':"name",
            'placeholder':"Client",}),
            
            'cuit' : TextInput(attrs={'class':"form-control",
            'id':"cuit",
            'placeholder':"CUIT",}),

            'website' : URLInput(attrs={'class':"form-control",
            'id':"website",
            'placeholder':"Website",}),

            'business_name' : TextInput(attrs={'class':"form-control",
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
            

            'c1_name' : TextInput(attrs={'class':"form-control",
            'id':"c1_name",
            'placeholder':"Full name",}),
            
            'c1_tel' : TextInput(attrs={
                'class':"form-control",
                'id':"c1_tel",
                'placeholder' : "Phone Number"
                }
            ),
            
            'c1_tel2' : TextInput(attrs={
                'class':"form-control",
                'id':"c1_tel2",
                'placeholder' : "Phone 2"
                }
            ),


            'c1_email' : EmailInput(attrs={
                'class':"form-control",
                'id':"c1_email",
                'placeholder' : "Email"
                }
            ),
            
            
            'c1_email2' : EmailInput(attrs={
                'class':"form-control",
                'id':"c1_email2",
                'placeholder' : "Email 2"
                }
            ),
            
            
            
            'c2_name' : TextInput(attrs={'class':"form-control",
            'id':"c2_name",
            'placeholder':"Full name",}),
            
            'c2_tel' : TextInput(attrs={
                'class':"form-control",
                'id':"c2_tel",
                'placeholder' : "Phone Number"
                }
            ),
            
            'c2_tel2' : TextInput(attrs={
                'class':"form-control",
                'id':"c2_tel2",
                'placeholder' : "Phone 2"
                }
            ),


            'c2_email' : EmailInput(attrs={
                'class':"form-control",
                'id':"c2_email",
                'placeholder' : "Email"
                }
            ),
            
            
            'c2_email2' : EmailInput(attrs={
                'class':"form-control",
                'id':"c2_email2",
                'placeholder' : "Email 2"
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
            
            'admin_tel2' : TextInput(attrs={
                'class':"form-control",
                'id':"admin_tel2",
                'placeholder' : "Phone 2"
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
            
            
            'landing_page' : URLInput(attrs={'class':"form-control",
            'id':"landing_page",
            'placeholder':"Landing Page",}),


        }
        




class EditClientForm(ModelForm):
    
    class Meta:
        model = Client
        
        exclude = ['id',]
        
        widgets = {

            'date' : TextInput(attrs={'class':"datetimepicker form-control",
            'id':"PublishDateTimeTextbox",
            'type':"date",
            'placeholder':"Date",}),


            'name' : TextInput(attrs={'class':"form-control",
            'id':"name",
            'placeholder':"Client",}),
            
            'cuit' : TextInput(attrs={'class':"form-control",
            'id':"cuit",
            'placeholder':"CUIT",}),

            'website' : URLInput(attrs={'class':"form-control",
            'id':"website",
            'placeholder':"Website",}),

            'business_name' : TextInput(attrs={'class':"form-control",
            'id':"business_name",
            'placeholder':"Business name",}),

            'source' : Select(attrs={
                'class':"default-select form-control wide mb-3",
                'id':"source",
                'placeholder' : "Source",
                'empty_label':"Select the source",
                }
            ),

            'wop' : Select(attrs={
                'class':"default-select form-control wide mb-3",
            'id':"wop",
            'placeholder':"WOP",}),

            
            'c1_name' : TextInput(attrs={'class':"form-control",
            'id':"c1_name",
            'placeholder':"Full name",}),
            
            'c1_tel' : TextInput(attrs={
                'class':"form-control",
                'id':"c1_tel",
                'placeholder' : "Phone Number"
                }
            ),
            
            'c1_tel2' : TextInput(attrs={
                'class':"form-control",
                'id':"c1_tel2",
                'placeholder' : "Phone 2"
                }
            ),


            'c1_email' : EmailInput(attrs={
                'class':"form-control",
                'id':"c1_email",
                'placeholder' : "Email"
                }
            ),
            
            
            'c1_email2' : EmailInput(attrs={
                'class':"form-control",
                'id':"c1_email2",
                'placeholder' : "Email 2"
                }
            ),
            
            
            
            'c2_name' : TextInput(attrs={'class':"form-control",
            'id':"c2_name",
            'placeholder':"Full name",}),
            
            'c2_tel' : TextInput(attrs={
                'class':"form-control",
                'id':"c2_tel",
                'placeholder' : "Phone Number"
                }
            ),
            
            'c2_tel2' : TextInput(attrs={
                'class':"form-control",
                'id':"c2_tel2",
                'placeholder' : "Phone 2"
                }
            ),


            'c2_email' : EmailInput(attrs={
                'class':"form-control",
                'id':"c2_email",
                'placeholder' : "Email"
                }
            ),
            
            
            'c2_email2' : EmailInput(attrs={
                'class':"form-control",
                'id':"c2_email2",
                'placeholder' : "Email 2"
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
            
            'admin_tel2' : TextInput(attrs={
                'class':"form-control",
                'id':"admin_tel2",
                'placeholder' : "Phone 2"
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

            'landing_page' : URLInput(attrs={'class':"form-control",
            'id':"landing_page",
            'placeholder':"Landing Page",}),
            
            
            'cancelled' : Select(attrs={
                'class':"form-select",
            'id':"cancelled",
            'placeholder':"Cancelled?",}),
            
            'date_can' : TextInput(attrs={'class':"datetimepicker form-control",
            'id':"PublishDateTimeTextbox",
            'type':"date",
            'placeholder':"Cancellation date",}),
            
            
            'fail_can' : Select(attrs={
                'class':"form-select",
            'id':"fail_can",
            'placeholder':"Do we fail?",}),
            
            
            'comment_can' : Textarea(attrs={
                'class':"form-control",
                'id':"comment_can",
                'placeholder' : "Comment"
                }
            ),


        }


"""