from statistics import mode
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

ALGORITHMS_LIST = (
    ("Decision Tree", "Decision Tree"),
    ("KNearestNeighbour", "KNearestNeighbour"),
    ("NaiveBayes", "NaiveBayes"),
    ("RandomForest", "RandomForest"),
)


class Prediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,
                             on_delete=models.CASCADE, blank=True, null=True)
    patient_name = models.CharField(max_length=250, null=True, blank=True)
    patient_id = models.CharField(max_length=250, null=True, blank=True)
    disease = models.CharField(max_length=250, null=True, blank=True)
    algorithm = models.CharField(max_length=250, null=True, blank=True)
    # algorithm      = models.CharField(_("Type of Algorithms"),max_length=250, choices=ALGORITHMS_LIST, blank=True, null=True)
    symptom_1 = models.CharField(
        _("Symptom 1"), max_length=250, null=True, blank=True)
    symptom_2 = models.CharField(
        _("Symptom 2"), max_length=250, null=True, blank=True)
    symptom_3 = models.CharField(
        _("Symptom 3"), max_length=250, null=True, blank=True)
    symptom_4 = models.CharField(
        _("Symptom 4"), max_length=250, null=True, blank=True)
    symptom_5 = models.CharField(
        _("Symptom 5"), max_length=250, null=True, blank=True)
    symptoms = models.JSONField(
        _("Collection of the symptoms"), default=dict, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.patient_name + ' - ' + self.disease

    class Meta:
        ordering = ["-timestamp", "-updated"]


class PredictionParameter(models.Model):
    user = models.ForeignKey(_("Name of the logged in user"), settings.AUTH_USER_MODEL, default=1,
                             on_delete=models.CASCADE, blank=True, null=True)
    disease = models.CharField(
        _("Name of the disease"), max_length=250, null=True, blank=True)
    avg_day = models.CharField(
        _("Average number of cases per day"), max_length=250, null=True, blank=True)
    avg_week = models.CharField(
        _("Average number of cases per week"), max_length=250, null=True, blank=True)
    avg_month = models.CharField(
        _("Average number of cases per month"), max_length=250, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.disease

    class Meta:
        ordering = ["-timestamp", "-updated"]
