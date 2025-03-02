from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Allows editing of order items inside the Order admin panel """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0  # Prevents Django from adding extra empty forms


class OrderAdmin(admin.ModelAdmin):
    """ Admin panel settings for Order management """
    
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total')

    fields = (
        'order_number', 'date', 'full_name', 'email', 
        'phone_number', 'country', 'postcode', 'town_or_city',
        'street_address1', 'street_address2', 'county', 
        'delivery_cost', 'order_total', 'grand_total',
    )

    list_display = ('order_number', 'date', 'full_name', 'email', 'order_total', 'delivery_cost', 'grand_total')

    list_filter = ('date', 'country',)
    
    search_fields = ('order_number', 'full_name', 'email', 'phone_number')

    ordering = ('-date', '-order_number')


admin.site.register(Order, OrderAdmin)
