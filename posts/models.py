from django.db import models
from userauth import models as userauthModel
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_on = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(userauthModel.Users,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Posts"

class Comments(models.Model):
    comment = models.CharField(max_length=200)
    posted_on = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(userauthModel.Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)