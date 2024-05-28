from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name="Telegram ID", unique=True, default=1)

    def __str__(self):
        return f"{self.id}.{self.telegram_id} - {self.full_name}"


class table_1(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=False, unique=True)
    file_id = models.CharField(verbose_name="File ID", max_length=50)
    file_name = models.CharField(verbose_name="File Name", max_length=150, null=True)
    file_type = models.CharField(verbose_name="File Type", max_length=10, null=True)
    caption = models.CharField(verbose_name="Caption", max_length=4000, null=True)

    def __str__(self):
        return f"{self.lesson_number}.{self.file_name} - {self.file_type}"

    class Meta:
        verbose_name = 'Psixoterapiya va psixologiya asoslari'
        verbose_name_plural = 'Psixoterapiya va psixologiya asoslari'


class table_2(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True, unique=True)
    file_id = models.CharField(verbose_name="File ID", max_length=50)
    file_name = models.CharField(verbose_name="File Name", max_length=150, null=True)
    file_type = models.CharField(verbose_name="File Type", max_length=10, null=True)
    caption = models.CharField(verbose_name="Caption", max_length=4000, null=True)

    def __str__(self):
        return f"{self.lesson_number}.{self.file_name} - {self.file_type}"

    class Meta:
        verbose_name = 'Tabobat va tibbiyotda mijoz va tepmerament ilmi'
        verbose_name_plural = 'Tabobat va tibbiyotda mijoz va tepmerament ilmi'


class table_3(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True, unique=True)
    file_id = models.CharField(verbose_name="File ID", max_length=50)
    file_name = models.CharField(verbose_name="File Name", max_length=150, null=True)
    file_type = models.CharField(verbose_name="File Type", max_length=10, null=True)
    caption = models.CharField(verbose_name="Caption", max_length=4000, null=True)

    def __str__(self):
        return f"{self.lesson_number}.{self.file_name} - {self.file_type}"

    class Meta:
        verbose_name = 'Miyaning neyroplastikligi va neyrobika'
        verbose_name_plural = 'Miyaning neyroplastikligi va neyrobika'


class table_4(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True, unique=True)
    file_id = models.CharField(verbose_name="File ID", max_length=50)
    file_name = models.CharField(verbose_name="File Name", max_length=150, null=True)
    file_type = models.CharField(verbose_name="File Type", max_length=10, null=True)
    caption = models.CharField(verbose_name="Caption", max_length=4000, null=True)

    def __str__(self):
        return f"{self.lesson_number}.{self.file_name} - {self.file_type}"

    class Meta:
        verbose_name = 'Ta\'lim va ruhiyat'
        verbose_name_plural = 'Ta\'lim va ruhiyat'


class table_5(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True, unique=True)
    file_id = models.CharField(verbose_name="File ID", max_length=50)
    file_name = models.CharField(verbose_name="File Name", max_length=150, null=True)
    file_type = models.CharField(verbose_name="File Type", max_length=10, null=True)
    caption = models.CharField(verbose_name="Caption", max_length=4000, null=True)

    def __str__(self):
        return f"{self.lesson_number}.{self.file_name} - {self.file_type}"

    class Meta:
        verbose_name = 'Farzandim va jigarbandim'
        verbose_name_plural = 'Farzandim va jigarbandim'


class table_6(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True, unique=True)
    file_id = models.CharField(verbose_name="File ID", max_length=50)
    file_name = models.CharField(verbose_name="File Name", max_length=150, null=True)
    file_type = models.CharField(verbose_name="File Type", max_length=10, null=True)
    caption = models.CharField(verbose_name="Caption", max_length=4000, null=True)

    def __str__(self):
        return f"{self.lesson_number}.{self.file_name} - {self.file_type}"

    class Meta:
        verbose_name = 'Nafs diagnostikasi'
        verbose_name_plural = 'Nafs diagnostikasi'


class table_7(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True, unique=True)
    file_id = models.CharField(verbose_name="File ID", max_length=50)
    file_name = models.CharField(verbose_name="File Name", max_length=150, null=True)
    file_type = models.CharField(verbose_name="File Type", max_length=10, null=True)
    caption = models.CharField(verbose_name="Caption", max_length=4000, null=True)

    def __str__(self):
        return f"{self.lesson_number}.{self.file_name} - {self.file_type}"

    class Meta:
        verbose_name = 'Sharq psixologiyasi va psixoterapiya'
        verbose_name_plural = 'Sharq psixologiyasi va psixoterapiya'


class table_8(models.Model):
    lesson_number = models.IntegerField(verbose_name="Dars tartib raqami", null=True, unique=True)
    file_id = models.CharField(verbose_name="File ID", max_length=50)
    file_name = models.CharField(verbose_name="File Name", max_length=150, null=True)
    file_type = models.CharField(verbose_name="File Type", max_length=10, null=True)
    caption = models.CharField(verbose_name="Caption", max_length=4000, null=True)

    def __str__(self):
        return f"{self.lesson_number}.{self.file_name} - {self.file_type}"

    class Meta:
        verbose_name = 'Ruhiy salomatlik'
        verbose_name_plural = 'Ruhiy salomatlik'


class Tables(models.Model):
    id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=30)
    comment_one = models.CharField(max_length=1000)
    files = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. {self.table_name}"

    class Meta:
        verbose_name = 'Darslar jadvali'
        verbose_name_plural = 'Darslar jadvali'
