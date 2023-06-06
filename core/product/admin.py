from django.contrib import admin
from .models import SongsManagementTable,AlbumManagementTable,SingerManagementTable,PlayListCreationTable,ImportTable,ExportTable,UserTable,GenreTable
from django.db import models
from django.utils.html import format_html
from django.forms import TextInput, Textarea, SelectMultiple, DateInput, CheckboxInput, Select


class SongsManagementTableAdmin(admin.ModelAdmin):
    list_display = ('id','song_title','song_poet','song_released_date','song_duration','song_album_id','song_photo')
    list_display_links = ('id','song_title','song_poet','song_released_date','song_duration','song_album_id','song_photo')
    list_filter = ('song_released_date','song_duration')
    search_fields = ('song_title',)
    sortable_by = ('id',)
    ordering = ('song_genre_id',)
    date_hierarchy = 'song_released_date'
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '150'})},
        models.DateField: {'widget': DateInput()},
    }
    def photo_display(self,obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.song_photo.url)

    photo_display.short_description = 'Song Photo'
    

class AlbumManagementTableAdmin(admin.ModelAdmin):
    list_display = ('id','album_name','album_info')
    list_display_links = ('id','album_name','album_info')
    list_filter = ('album_name',)
    search_fields = ('album_name',)
    sortable_by = ('id',)
    ordering = ('album_name',)


class SingerManagementTableAdmin(admin.ModelAdmin):
    list_display = ('id','singer_name','singer_info')
    list_display_links = ('id','singer_name','singer_info')
    search_fields = ('singer_name',)
    sortable_by = ('id',)
    ordering = ('singer_name',)
    

class PlayListCreationTableAdmin(admin.ModelAdmin):
    list_display = ('id','playlist_song_id','playlist_album_id')
    list_display_links = ('id','playlist_song_id','playlist_album_id')
    list_filter = ('playlist_album_id',)
    sortable_by = ('id',)
    
class ImportTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at') 
    list_display_links = ('id', 'created_at')
    search_fields = ('name',)
    sortable_by = ('id',)

class ExportTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'format', 'file', 'created_at')
    list_display_links = ('id', 'format', 'file', 'created_at')
    list_filter = ('format',)
    sortable_by = ('id',)

class GenreTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name',)
    sortable_by = ('genre_name',)
    ordering = ('id',)

class ExportTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'format', 'file', 'created_at')
    list_display_links = ('id', 'format', 'file', 'created_at')
    list_filter = ('format',)
    sortable_by = ('id',)

class GenreTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name',)
    sortable_by = ('id',)

class UserTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name',)
    sortable_by = ('id',)


admin.site.register(SongsManagementTable,SongsManagementTableAdmin)
admin.site.register(AlbumManagementTable,AlbumManagementTableAdmin)
admin.site.register(SingerManagementTable,SingerManagementTableAdmin)
admin.site.register(PlayListCreationTable,PlayListCreationTableAdmin)
admin.site.register(ImportTable,ImportTableAdmin)
admin.site.register(ExportTable,ExportTableAdmin)
admin.site.register(UserTable,UserTableAdmin) # Because we define it before...
admin.site.register(GenreTable,GenreTableAdmin)
