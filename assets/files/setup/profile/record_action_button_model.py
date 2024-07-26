# models.py
from django.db import models

class RecordActionButton(models.Model):
    class action_types(models.TextChoices):
        SINGLE = 'single', _("Single")
        MULTIPLE = 'multi', _("Multiple")
        def __str__(self):
            return self.value

    name = models.CharField(max_length=100, unique=True)
    icon_colour = models.CharField(max_length=100, blank=True, null=True, help_text="Colour of the icon")
    title = models.CharField(max_length=100,  blank=True, null=True)
    label = models.CharField(max_length=100,  blank=True, null=True)
    type = models.CharField(max_length=100, choices=action_types.choices, default=action_types.SINGLE, blank=True, null=True )
    error_message = models.CharField(max_length=100, blank=True, null=True)
    icon_class = models.CharField(max_length=100, help_text="Font Awesome icon class", blank=True, null=True)
    action = models.CharField(max_length=100, help_text="Name of javascript function to be performed on click", blank=True, null=True)

    def __str__(self):
        return self.name + " : " + self.title + " : " + self.type

    def create_record_action_button(self, name, title, label, type, error_message, icon_class, action, icon_colour):
        self.name = name
        self.title = title
        self.label = label
        self.type = type
        self.error_message = error_message
        self.icon_class = icon_class
        self.action = action
        self.icon_colour = icon_colour
        self.save()
        return self
