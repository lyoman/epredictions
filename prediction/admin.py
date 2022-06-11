from django.contrib import admin
from . models import Prediction, PredictionParameter

class PredictionModelAdmin(admin.ModelAdmin):
    list_display        = [
                           "user", 
                           "patient_name", 
                           "patient_id", 
                           "disease",
                           "symptom_1", 
                           "symptom_2",
                           "symptom_3", 
                           "symptom_4",
                           "symptom_5",
                           "symptoms", 
                           "timestamp",
                           "updated"
                           ]
    list_display_links  = ["updated", "timestamp", "user", "patient_name", "disease"]
    list_editable       = ["patient_id"]
    list_filter         = ["updated", "timestamp", "disease", "patient_name"]
    search_fields       = ["patient_name", "disease"]
    class Meta:
        model = Prediction
        
class PredictionParameterModelAdmin(admin.ModelAdmin):
    list_display        = [
                           "user", 
                           "disease",
                           "age",
                           "gender",
                           "avg_day", 
                           "avg_week", 
                           "avg_month",
                           "timestamp",
                           "updated"
                           ]
    list_display_links  = ["updated", "timestamp", "user", "disease"]
    list_editable       = ["avg_day", "avg_week", "avg_month"]
    list_filter         = ["updated", "timestamp", "disease", "gender", "age"]
    search_fields       = ["disease"]
    class Meta:
        model = PredictionParameter

admin.site.register(Prediction, PredictionModelAdmin)
admin.site.register(PredictionParameter, PredictionParameterModelAdmin)
