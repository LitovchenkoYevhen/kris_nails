from django.contrib import admin

from .models import Services, Cleaning, Nails

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'content', 'updated_at', 'price', 'is_published']
    list_display_links = ['service_name', 'content', 'price']
    list_editable = ('is_published',)

class CleaningAdmin(admin.ModelAdmin):
    list_display = ['step_name', 'created_at', 'updated_at', 'is_published']
    list_display_links = ['step_name', 'created_at', 'updated_at']
    list_editable = ('is_published',)

admin.site.register(Services, ServicesAdmin)
admin.site.register(Cleaning, CleaningAdmin)
admin.site.register(Nails)
