# models.py
from django.db import models
from .title_button_model import TitleButton
from .record_action_button_model import RecordActionButton
class Component(models.Model):
    class Meta:
        ordering = ['title']

    title_buttons = models.ManyToManyField(TitleButton, blank=True)
    recordaction_buttons = models.ManyToManyField(RecordActionButton, blank=True)
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    widget_icon = models.CharField(max_length=100, blank=True, null=True)
    widget_colour = models.CharField(max_length=200,blank=True, null=True)
    widget_icon_class = models.CharField(max_length=100, blank=True, null=True)
    table_id = models.CharField(max_length=100)
    reverse_url = models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):
        return self.name + " : " + self.title

    def create_component(self, name, title, subtitle, widget_icon, widget_colour, widget_icon_class, table_id, reverse_url):
        self.name = name
        self.title = title
        self.subtitle = subtitle
        self.widget_icon = widget_icon
        self.widget_colour = widget_colour
        self.widget_icon_class = widget_icon_class
        self.table_id = table_id
        self.reverse_url = reverse_url
        self.save()
        return self