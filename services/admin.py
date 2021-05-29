from django.contrib import admin

from .models import Services, Cleaning, Visits, Clients

# class ServicesAdmin(admin.ModelAdmin):
#     list_display = ['service_name', 'content', 'updated_at', 'price', 'is_published']
#     list_display_links = ['service_name', 'content', 'price']
#     list_editable = ('is_published',)
#
# class CleaningAdmin(admin.ModelAdmin):
#     list_display = ['step_name', 'created_at', 'updated_at', 'is_published']
#     list_display_links = ['step_name', 'created_at', 'updated_at']
#     list_editable = ('is_published',)

class VisitsAdmin(admin.ModelAdmin):
    list_display = ['service_name','client', 'work_date',]
    list_display_links = ['service_name', 'client', 'work_date',]


admin.site.register(Services)
admin.site.register(Cleaning)
admin.site.register(Visits, VisitsAdmin)
admin.site.register(Clients)
