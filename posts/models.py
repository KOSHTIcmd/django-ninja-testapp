from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        #return super().__str__()
        return self.title
