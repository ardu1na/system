
from django.contrib import admin

from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin

from comercial.models import Sale, Adj, Subscription, Product, Income, Client, SetTier
from comercial.resources import SaleResource, AdjResource,\
    SubResource, IncomeResource, ProductResource, ClientResource



admin.site.site_header = 'DJANGO ARDU1NA ERP'
admin.site.index_title = 'Home'
admin.site.site_title = 'ADMIN'


class SaleInstanceInline(admin.TabularInline):
    model = Sale
    extra = 0
    show_change_link = True
    class Meta:
        verbose_name_plural = "SALES"
        verbose_name= "SALE"


class ClientAdmin(ModelAdmin, ImportExportModelAdmin):
    inlines = [SaleInstanceInline,]
    resource_class = ClientResource 
    
admin.site.register(Client, ClientAdmin)


admin.site.register(SetTier)


class SaleAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_class = SaleResource
    list_display = ['product', 'client', 'price', 'status', 'kind', 'note', 'created_at']
    search_fields = ['note', 'client', 'product']
    list_filter = ['status', 'kind']
admin.site.register(Sale, SaleAdmin)





class AdjAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_class = AdjResource 
    list_display = ['type', 'service', 'client', 'adj_percent', 'notice_date', 'email_date']
    search_fields = ['client', 'service']
    list_filter = ['type',]
admin.site.register(Adj, AdjAdmin)


class SubAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_class = SubResource
    list_display = ['service', 'client', 'total', 'cancelled', 'created_at']
    search_fields = ['client', 'service']
    list_filter = ['cancelled',]

admin.site.register(Subscription, SubAdmin)


class IncomeAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_class = IncomeResource
    list_display = ['amount', 'sale', 'subscription', 'date']
    
    search_fields = ['subscription', 'sale']
admin.site.register(Income, IncomeAdmin)



class ProductAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_class = ProductResource

    list_display = ['name', 'is_rr']
admin.site.register(Product, ProductAdmin)

    
    