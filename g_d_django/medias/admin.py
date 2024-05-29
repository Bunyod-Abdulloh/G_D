from django.contrib import admin
from django.http import HttpResponse

# Register your models here.
from .models import User, table_1, table_2, table_3, table_4, table_5, table_6, table_7, table_8, table_9


class CommonAdmin(admin.ModelAdmin):
    list_display = ('lesson_number', 'file_name', 'caption')
    ordering = ('lesson_number',)


admin.site.register(table_1, CommonAdmin)
admin.site.register(table_2, CommonAdmin)
admin.site.register(table_3, CommonAdmin)
admin.site.register(table_4, CommonAdmin)
admin.site.register(table_5, CommonAdmin)
admin.site.register(table_6, CommonAdmin)
admin.site.register(table_7, CommonAdmin)
admin.site.register(table_8, CommonAdmin)
admin.site.register(table_9, CommonAdmin)
admin.site.register(User)
