from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date_at = models.DateField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True, upload_to='post')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    name = models.ForeignKey(Author,on_delete=models.CASCADE)
    date_at = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    post = models.TextField()

    def __str__(self):
        return self.title
