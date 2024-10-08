from django.urls import path 
from . import views

urlpatterns = [
    path("", views.loginn),
    path("logout/",views.logoutt),
    path("purchase_report/", views.purchase_report, name='purchase_report'),
    path("sales_report/", views.sales_report),
    path("product_report/", views.product_report),
    path("stock_report/", views.stock_report),
    path("collection_report/", views.collection_report),
    path("refund_report/", views.refund_report),
    path("add_unit/", views.add_unit),
    path('update_unit/<int:id>', views.update_unit),
    path('unit_report/', views.unit_report),
    path('user_list/', views.user_list),
    path("add_user/", views.add_user),
    path("update_user/<int:id>", views.update_user),
    path("add_product/", views.add_product),
    path("update_product/<int:id>", views.update_product),
    path("add_purchase/", views.add_purchase),
    path("add_vendor/", views.add_vendor),
    path('check_vendor_exists/', views.check_vendor_exists, name='check_vendor_exists'),
    path('update_vendor/<int:id>', views.update_vendor),
    path('vendor_report/', views.vendor_report),
    path('home/', views.home),
    path('expiry_report/', views.expiry_report),
    path('sales_channel/', views.sales_channel),
    path('api/products/', views.api_products, name='product_list_api'),
    path('api/add_to_holdsale/', views.add_to_holdsale, name='add_to_holdsale'),
    path('api/delete_hold_items/', views.delete_hold_items, name='delete_hold_items'),
    path('api/get_hold_items/', views.get_hold_items, name='get_hold_items'),
    path('api/update_hold_item/', views.update_hold_item, name='update_hold_item_quantity'),
    path('update-channel/', views.update_channel_and_invoice, name='update_channel_to_sale'),
    path('update-channel-fonepay/', views.update_channel_and_invoice_fonepay, name='update_channel_to_sale_fonepay'),
    path('update-channel-card/', views.update_channel_and_invoice_card, name='update_channel_to_sale_card'),


]