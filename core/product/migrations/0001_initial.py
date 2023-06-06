# Generated by Django 4.2.1 on 2023-06-06 06:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AlbumManagementTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Id"
                    ),
                ),
                (
                    "album_name",
                    models.CharField(max_length=100, verbose_name="Album Name"),
                ),
                (
                    "album_info",
                    models.TextField(
                        max_length=200, verbose_name="Additional Information"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExportTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "format",
                    models.CharField(max_length=50, verbose_name="Export Format"),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="core/media/export/", verbose_name="Exported File"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GenreTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Id"
                    ),
                ),
                (
                    "genre_name",
                    models.CharField(max_length=100, verbose_name="Genre Name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImportTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="core/media/import/", verbose_name="Imported File"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SingerManagementTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Id"
                    ),
                ),
                (
                    "singer_name",
                    models.CharField(max_length=100, verbose_name="Singer Name"),
                ),
                (
                    "singer_info",
                    models.TextField(max_length=200, verbose_name="Singer Information"),
                ),
                (
                    "singer_genre_id",
                    models.ManyToManyField(
                        default="",
                        to="product.genretable",
                        verbose_name="Singer Genre Id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SongsManagementTable",
            fields=[
                (
                    "song_released_date",
                    models.DateField(
                        auto_created=True, default="", verbose_name="Released Year"
                    ),
                ),
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Id"
                    ),
                ),
                (
                    "song_title",
                    models.CharField(max_length=100, verbose_name="Song Tile"),
                ),
                (
                    "song_poet",
                    models.CharField(max_length=100, verbose_name="Poet Name"),
                ),
                (
                    "song_duration",
                    models.CharField(max_length=100, verbose_name="Duration"),
                ),
                (
                    "song_additional_info",
                    models.TextField(
                        max_length=200, verbose_name="Additional Information"
                    ),
                ),
                (
                    "song_photo",
                    models.ImageField(
                        blank=True,
                        upload_to="media/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png"]
                            )
                        ],
                        verbose_name="Song Photo",
                    ),
                ),
                (
                    "song_album_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.albummanagementtable",
                        verbose_name="Album Id",
                    ),
                ),
                (
                    "song_genre_id",
                    models.ManyToManyField(
                        default="", to="product.genretable", verbose_name="Genre Id"
                    ),
                ),
                (
                    "song_singer_id",
                    models.ManyToManyField(
                        default="",
                        to="product.singermanagementtable",
                        verbose_name="Singer Id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Id"
                    ),
                ),
                (
                    "user_name",
                    models.CharField(max_length=100, verbose_name="User Name"),
                ),
                (
                    "user_favorite_genre_id",
                    models.ManyToManyField(
                        default="",
                        to="product.genretable",
                        verbose_name="Favorite Genre Id",
                    ),
                ),
                (
                    "user_most_played_song_id",
                    models.ManyToManyField(
                        default="",
                        to="product.songsmanagementtable",
                        verbose_name="Most Played Songs Id",
                    ),
                ),
                (
                    "user_similar_artists_id",
                    models.ManyToManyField(
                        default="",
                        to="product.singermanagementtable",
                        verbose_name="Similar Artists Id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlayListCreationTable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Id"
                    ),
                ),
                (
                    "playlist_album_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.albummanagementtable",
                        verbose_name="Playlist Album Id",
                    ),
                ),
                (
                    "playlist_singer_id",
                    models.ManyToManyField(
                        default="",
                        related_name="PlayListCreation",
                        to="product.singermanagementtable",
                        verbose_name="Playlist Singer Id",
                    ),
                ),
                (
                    "playlist_song_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.singermanagementtable",
                        verbose_name="Playlist Song Id",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="albummanagementtable",
            name="album_singer_id",
            field=models.ManyToManyField(
                default="", to="product.singermanagementtable", verbose_name="Artist Id"
            ),
        ),
    ]