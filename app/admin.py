from cProfile import Profile
from django.contrib import admin

from django.contrib.auth.models import User
from .models import Stock, StockMovement, Unit, Product, Vendor,Holdsale,Collectionsale,Profile




class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'get_user_type', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

    def get_user_type(self, obj):
        return obj.profile.user_type
    get_user_type.short_description = 'User Type'

# Unregister the default User admin
admin.site.unregister(User)
admin.site.register(Profile)
# Register the new User admin
admin.site.register(User, UserAdmin)

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
class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'



