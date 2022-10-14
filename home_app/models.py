from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

class testimony(models.Model): #creates a table or model on the database
    Testimony_Name = models.CharField(max_length=200, verbose_name="Nombre del que hace el testimonio")
    content = tinymce_models.HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self): #it calls itself to show the data more clear
        return self.Testimony_Name