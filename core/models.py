from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("topic_list", args=[str(self.id)])

    def get_slug(self):
        self.slug = slugify(self.name)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1500, null=True, blank=True)
    book_url = models.URLField(max_length=200, null=True, blank=True)
    date_added = models.DateField('Date Added',auto_now_add=True, null=True, blank=True)
    book_topic = models.ManyToManyField(Topic, related_name='book_topics')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-date_added']
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"slug": self.slug})
    
    def get_slug(self):
        if self.slug:
            return
        self.slug = slugify(self.title)
        

    def __str__(self):
        """String representation."""
        return self.title

    def display_book_topic(self):
        """Create a string for the topics of each book"""
        return ', '.join(book_topic.name for book_topic in self.book_topic.all())

    display_book_topic.short_description = "Topic"
