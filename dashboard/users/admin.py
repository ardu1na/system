from django.contrib import admin
from dashboard.users.models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
	model = CustomUser
	search_fields = ('email','first_name','last_name',)
	list_filter = ('email','first_name','last_name','is_active','is_staff')
	list_display=('username','email','first_name','last_name','is_active','is_staff')

	fieldsets=(
			(None,{'fields':('username','email', 'first_name','last_name',)}),
			('Permissions',{'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
		)

	add_fieldsets = (
	(None,{
		'classes':('wide',),
		'fields':('username','email','first_name','last_name','password1','password2','is_active','is_staff','groups','user_permissions')
		}
		),
	)

admin.site.register(CustomUser,UserAdminConfig)