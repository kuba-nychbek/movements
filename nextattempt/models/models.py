from django.db import models

class Mine(models.model):
    title = models.CharField(null=False, verbose_name='title')
    describtion = models.TextField(null=False, verbose_name='describtion')
    date = models.DateField(auto_now=False, auto_created=True, auto_now_add=False)
    
    def __str__(self)-> str:
        return  f'{self.id}. {self.title}:{self.describtion}'
    
