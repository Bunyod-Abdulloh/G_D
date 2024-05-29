from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name="Telegram ID", unique=True, default=1)

    def __str__(self):
        return f"{self.id}.{self.telegram_id} - {self.full_name}"


class table_1(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=False)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=4000, null=True)

    class Meta:
        verbose_name = 'Psixoterapiya va psixologiya asoslari'
        verbose_name_plural = 'Psixoterapiya va psixologiya asoslari'


class table_2(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=50, null=True)

    class Meta:
        verbose_name = 'Tabobat va tibbiyotda mijoz va tepmerament ilmi'
        verbose_name_plural = 'Tabobat va tibbiyotda mijoz va tepmerament ilmi'


class table_3(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=50, null=True)

    class Meta:
        verbose_name = 'Miyaning neyroplastikligi va neyrobika'
        verbose_name_plural = 'Miyaning neyroplastikligi va neyrobika'


class table_4(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=50, null=True)

    class Meta:
        verbose_name = 'Ta\'lim va ruhiyat'
        verbose_name_plural = 'Ta\'lim va ruhiyat'


class table_5(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=50, null=True)

    class Meta:
        verbose_name = 'Farzandim va jigarbandim'
        verbose_name_plural = 'Farzandim va jigarbandim'


class table_6(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=50, null=True)

    class Meta:
        verbose_name = 'Nafs diagnostikasi'
        verbose_name_plural = 'Nafs diagnostikasi'


class table_7(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=50, null=True)

    class Meta:
        verbose_name = 'Sharq psixologiyasi va psixoterapiya'
        verbose_name_plural = 'Sharq psixologiyasi va psixoterapiya'


class table_8(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=50, null=True)

    class Meta:
        verbose_name = 'Ruhiy salomatlik'
        verbose_name_plural = 'Ruhiy salomatlik'


class table_9(models.Model):
    lesson_number = models.IntegerField(verbose_name="Suhbat tartib raqami", null=True)
    audio_id = models.CharField(verbose_name="Audio ID", max_length=50, blank=True)
    photo_id = models.CharField(verbose_name="Rasm ID", max_length=50, blank=True)
    video_id = models.CharField(verbose_name="Video ID", max_length=50, blank=True)
    document_id = models.CharField(verbose_name="Document ID", max_length=50, blank=True)
    file_name = models.CharField(verbose_name="Fayl nomi", max_length=150, null=True)
    caption = models.CharField(verbose_name="Tavsif", max_length=50, null=True)

    class Meta:
        verbose_name = 'Turli suhbatlar'
        verbose_name_plural = 'Turli suhbatlar'

