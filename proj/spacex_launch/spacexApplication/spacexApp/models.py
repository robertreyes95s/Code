from django.db import models

class futureLaunch(models.Model):
    title = models.CharField(max_length = 200)
    launch_date = models.DateTimeField()
    launch_site = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    

    def __str__(self):
        return str(self.title)
   
    class Meta:
        ordering = ['title']

    class Admin:
        pass
    