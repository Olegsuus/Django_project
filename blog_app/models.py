from django.db import models


class Author(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField()
    text = models.CharField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    text = models.CharField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)








