from django.db import models

# Create your models here.

class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200)

    def __str__(self):
        """String representation."""
        return self.title

