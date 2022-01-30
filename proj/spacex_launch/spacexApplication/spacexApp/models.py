from django.db import models

class futureLaunch(models.Model):
    title = models.CharField(max_length = 200)
    launch_date_local = models.DateTimeField()
    

    def __str__(self):
        return str(self.name)
    