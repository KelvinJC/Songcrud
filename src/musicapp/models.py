from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class Song(models.Model):
    title = models.CharField('Song title', max_length=120)
    date_released = models.DateTimeField('Release date')
    likes = models.IntegerField(blank=True, null=True)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField('Lyrics', blank=True)
