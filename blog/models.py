from django.db import models

# Create your models here.


class Files(models.Model):
    file = models.FileField(upload_to="file")

    def __str__(self):
        return self.f_name