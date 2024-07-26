#models.py
from django.db import models

class TitleButton(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50, unique=True)
    template = models.CharField(max_length=500)
    additional_attr = models.CharField(max_length=500, blank=True, null=True,
                                       help_text="Additional attributes for the button,format: key1:value1,key2:value2,key3:value3")

    def __str__(self):
        return self.name

    def create_title_button(self, name, template, additional_attr):
        self.name = name
        self.template = template
        self.additional_attr = additional_attr
        self.save()
        return self