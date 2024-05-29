# Generated by Django 3.2.8 on 2024-05-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0013_auto_20240529_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_1',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_1',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='table_2',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_2',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='table_3',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_3',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='table_4',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_4',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='table_5',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_5',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='table_6',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_6',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='table_7',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_7',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='table_8',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_8',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='table_9',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='table_9',
            name='file_type',
        ),
        migrations.AddField(
            model_name='table_1',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_1',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_1',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_1',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
        migrations.AddField(
            model_name='table_2',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_2',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_2',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_2',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
        migrations.AddField(
            model_name='table_3',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_3',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_3',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_3',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
        migrations.AddField(
            model_name='table_4',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_4',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_4',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_4',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
        migrations.AddField(
            model_name='table_5',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_5',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_5',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_5',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
        migrations.AddField(
            model_name='table_6',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_6',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_6',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_6',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
        migrations.AddField(
            model_name='table_7',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_7',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_7',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_7',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
        migrations.AddField(
            model_name='table_8',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_8',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_8',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_8',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
        migrations.AddField(
            model_name='table_9',
            name='audio_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Audio ID'),
        ),
        migrations.AddField(
            model_name='table_9',
            name='document_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Document ID'),
        ),
        migrations.AddField(
            model_name='table_9',
            name='photo_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Rasm ID'),
        ),
        migrations.AddField(
            model_name='table_9',
            name='video_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Video ID'),
        ),
    ]