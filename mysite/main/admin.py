from django.contrib import admin
from .models import SiteName, HomeBg, Info, Product, AboutClient, Client, Contact
# Register your models here.

admin.site.register(SiteName)
admin.site.register(HomeBg)
admin.site.register(Info)
admin.site.register(Product)
admin.site.register(AboutClient)
admin.site.register(Client)
admin.site.register(Contact)