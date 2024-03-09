from django.db import models

# Category model
class Category(models.Model):
    title = models.CharField(max_length=150)
    category_image = models.ImageField(upload_to='imgs/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'


# News model
class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    details = models.TextField()
    image = models.ImageField(upload_to='imgs/')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment