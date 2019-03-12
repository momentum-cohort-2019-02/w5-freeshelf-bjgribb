from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/', null=True)
    book_url = models.URLField(max_length=200, null=True, blank=True)
    date_added = models.DateField('Date Added',auto_now_add=True)
    topics = models.ManyToManyField(Topic, verbose_name="topics")

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        """String representation."""
        return self.title
