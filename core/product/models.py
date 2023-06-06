from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator

class SongsManagementTable(models.Model):
    
    id = models.AutoField(primary_key=True, verbose_name="Id")
    song_title = models.CharField(max_length=100, verbose_name="Song Tile")
    song_poet = models.CharField(max_length=100, verbose_name="Poet Name")
    song_singer_id = models.ManyToManyField('SingerManagementTable', default='', verbose_name="Singer Id")
    song_genre_id = models.ManyToManyField('GenreTable', default='', verbose_name="Genre Id")
    song_released_date = models.DateField(auto_created=True,  default='',verbose_name="Released Year")
    song_duration = models.CharField(max_length=100, verbose_name="Duration")
    song_album_id= models.ForeignKey('AlbumManagementTable', on_delete=models.CASCADE, verbose_name="Album Id")
    song_additional_info = models.TextField(max_length=200, verbose_name="Additional Information")
    song_photo = models.ImageField(upload_to='media/',blank=True, validators=[FileExtensionValidator(['jpg', 'png'])],verbose_name="Song Photo")

    def __str__(self):
        return self.song_title
    
class AlbumManagementTable(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    album_name = models.CharField(max_length=100, verbose_name="Album Name")
    album_singer_id = models.ManyToManyField('SingerManagementTable',default='', verbose_name="Artist Id")
    album_info = models.TextField(max_length=200, verbose_name="Additional Information")
    
    def __str__(self):
        return self.album_name

class SingerManagementTable(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    singer_name = models.CharField(max_length=100, verbose_name="Singer Name")
    singer_genre_id = models.ManyToManyField('GenreTable',default='', verbose_name="Singer Genre Id")
    singer_info = models.TextField(max_length=200, verbose_name="Singer Information")
    
    def __str__(self):
        return self.singer_name
    
class PlayListCreationTable(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    playlist_song_id = models.ForeignKey('SingerManagementTable',on_delete=models.CASCADE, verbose_name="Playlist Song Id")
    playlist_album_id = models.ForeignKey('AlbumManagementTable',on_delete=models.CASCADE, verbose_name="Playlist Album Id")
    playlist_singer_id = models.ManyToManyField('SingerManagementTable',default='', verbose_name="Playlist Singer Id", related_name='PlayListCreation')
    

class ImportTable(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    file = models.FileField(upload_to='core/media/import/', verbose_name="Imported File")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"Import {self.id}"


class ExportTable(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    format = models.CharField(max_length=50, verbose_name="Export Format")
    file = models.FileField(upload_to='core/media/export/', verbose_name="Exported File")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"Export {self.id}"


class UserTable(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    user_name = models.CharField(max_length=100, verbose_name="User Name")
    user_favorite_genre_id = models.ManyToManyField('GenreTable', default='', verbose_name="Favorite Genre Id")
    user_most_played_song_id = models.ManyToManyField('SongsManagementTable', default='', verbose_name="Most Played Songs Id")
    user_similar_artists_id = models.ManyToManyField('SingerManagementTable',default='', verbose_name="Similar Artists Id")

    def __str__(self):
        return self.user_name
    
class GenreTable(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    genre_name = models.CharField(max_length=100, verbose_name="Genre Name")
    
    def __str__(self):
        return self.genre_name