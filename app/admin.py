from django.contrib import admin
from .models import Stock, StockMovement, Unit, Product, Vendor,Holdsale,Collectionsale

class UnitAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'ShortName', 'Status','User')  # Fields to display in list view
    search_fields = ('FullName', 'ShortName')  # Fields to be searchable
    list_filter = ('Status',)  # Sidebar filters for the list view
    ordering = ('FullName',)  # Default ordering of items


# Register the model with the custom admin class
admin.site.register(Unit, UnitAdmin)
admin.site.register(Product)
# admin.site.register(Stock)
admin.site.register(StockMovement)

# admin.site.register(Holdsale)
admin.site.register(Vendor)
admin.site.register(Collectionsale)