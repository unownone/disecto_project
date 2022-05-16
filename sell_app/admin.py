from django.contrib import admin
from sell_app.models import Item, Purchase, Purchased_item

# Register your models here.
admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(Purchased_item)
