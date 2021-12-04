from django.db import models
from datetime import date

from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100 , unique=True )

    def __str__(self) -> str:
        return self.category_name
        
class Todo(models.Model):
    category = models.ForeignKey(Category , on_delete = CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    Scheduling = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.title