from django.contrib import admin

from .models import TwoFactorAuth

admin.site.site_header = '2FA Admin'
admin.site.site_title = '2FA Admin' 
admin.site.index_title = '2FA Administration'
admin.site.register(TwoFactorAuth)
# Register your models here.

