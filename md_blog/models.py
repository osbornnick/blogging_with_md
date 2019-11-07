from django.db import models
import markdown


class Post(models.Model):
    title = models.CharField(max_length=255)
    md_path = models.CharField(max_length=255)
    html = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def save(self, *args, **kwargs):
        file = open(self.md_path, mode='r')
        self.html = markdown.markdown(file.read())
        file.close()
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=20)
