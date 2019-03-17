from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Topic(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    
    def get_absolute_url(self):
        return reverse('topic_list', kwargs={"slug": self.slug})

    # def save(self): not overriding default save or something
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super(Topic, self).save()

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book"""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1500, null=True, blank=True)
    book_url = models.URLField(max_length=200, null=True, blank=True)
    date_added = models.DateField('Date Added',auto_now_add=True, null=True, blank=True)
    topics = models.ManyToManyField(Topic)
    slug = models.SlugField()

    favorited_by = models.ManyToManyField(
        to=User, related_name="favorite_books", through='Favorite')

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

    def display_topics(self):
        """Create a string for the topics of each book"""
        return ', '.join(topic.name for topic in self.topics.all())

    display_topics.short_description = "Topic"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)
