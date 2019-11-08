from django.db import models
import markdown


class Post(models.Model):
    title = models.CharField(max_length=255)
    md_path = models.CharField(max_length=255)
    html = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        file = open(self.md_path, mode='r')
        self.html = markdown.markdown(file.read())
        file.close()
        super().save(*args, **kwargs)


class Post2(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    md = models.FileField(null=True)

    def __str__(self):
        return self.title

# md_path = './md_blog/static/TEST.md'
