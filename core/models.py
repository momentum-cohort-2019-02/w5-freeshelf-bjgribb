from django.db import models

# Create your models here.

class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    book_url = models.URLField(max_length=200, null=True)
    date_added = models.DateField('Date Added',auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        """String representation."""
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    pass
