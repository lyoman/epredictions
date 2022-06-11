from django.contrib import admin
from . models import DrugSearch

# Register your models here.
class DrugSearchModelAdmin(admin.ModelAdmin):
    list_display        = [
                           "name", 
                           "location", 
                           "latitude",
                           "longitude",
                           "timestamp", 
                           "updated"
                           ]
    list_display_links  = ["updated", "timestamp", "name"]
    list_editable       = ["location"]
    list_filter         = ["updated", "timestamp", "name"]
    search_fields       = ["name"]
    class Meta:
        model = DrugSearch
        
admin.site.register(DrugSearch, DrugSearchModelAdmin)