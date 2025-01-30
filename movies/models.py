from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name