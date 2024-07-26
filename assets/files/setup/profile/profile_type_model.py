#models.py
from django.db import models
from .component_model import Component

class ProfileType(models.Model):
    class Meta:
        ordering = ['description']

    components = models.ManyToManyField(Component, blank=True)
    type = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    widget_colour = models.CharField(max_length=200, blank=True, null=True)
    is_dtol_profile = models.BooleanField(default=False)
    is_permission_required = models.BooleanField(default=True)

    def __str__(self):
        return self.type + " : " + self.description

    def create_profile_type(self, type, description, widget_colour, is_dtol_profile, is_permission_required):
        self.type = type
        self.description = description
        self.widget_colour = widget_colour
        self.is_dtol_profile = is_dtol_profile
        self.is_permission_required = is_permission_required
        self.save()
        return self