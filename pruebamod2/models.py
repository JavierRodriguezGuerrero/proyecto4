from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Publication'
        verbose_name = 'Publication'
        ordering = ['title']
    


class Article2(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
    class Meta:
        db_table = 'Article2'
        verbose_name = 'Article2'
        ordering = ['headline']