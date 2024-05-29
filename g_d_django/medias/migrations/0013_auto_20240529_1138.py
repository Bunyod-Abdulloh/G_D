# Generated by Django 3.2.8 on 2024-05-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0012_auto_20240529_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table_1',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_1',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_1',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_1',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_2',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_2',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_2',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_2',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_3',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_3',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_3',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_3',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_4',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_4',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_4',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_4',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_5',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_5',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_5',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_5',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_6',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_6',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_6',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_6',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_7',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_7',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_7',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_7',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_8',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_8',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_8',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_8',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_9',
            name='caption',
            field=models.CharField(max_length=4000, null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='table_9',
            name='file_id',
            field=models.CharField(max_length=50, verbose_name='Fayl ID'),
        ),
        migrations.AlterField(
            model_name='table_9',
            name='file_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Fayl nomi'),
        ),
        migrations.AlterField(
            model_name='table_9',
            name='file_type',
            field=models.CharField(max_length=10, null=True, verbose_name='Fayl turi'),
        ),
        migrations.AlterField(
            model_name='table_9',
            name='lesson_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Suhbat tartib raqami'),
        ),
    ]