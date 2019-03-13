from django.db import models
from django.urls import reverse

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1500, null=True, blank=True)
    # picture = models.ImageField(upload_to='pictures/', null=True)
    book_url = models.URLField(max_length=200, null=True, blank=True)
    date_added = models.DateField('Date Added',auto_now_add=True)
    topics = models.ManyToManyField(Topic, verbose_name="topics")
    # slug = models.SlugField(null=True)

    class Meta:
        ordering = ['-date_added']
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def __str__(self):
        """String representation."""
        return self.title

    def display_topics(self):
        """Create a string for the topics of each book"""
        return ', '.join(topics.name for topics in self.topics.all())

    display_topics.short_description = "Topic"
