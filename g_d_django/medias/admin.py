from django.contrib import admin
from .models import User, Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8, Table9, Tables


class CommonAdmin(admin.ModelAdmin):
    list_display = ('lesson_number', 'file_name', 'caption')
    ordering = ('lesson_number',)


class CommonAdminTwo(admin.ModelAdmin):
    list_display = ('table_number', 'table_name', 'files')
    ordering = ('table_number',)


tables = [Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8]

for table in tables:
    admin.site.register(table, CommonAdmin)

admin.site.register(Table9, CommonAdmin)
admin.site.register(Tables, CommonAdminTwo)
admin.site.register(User)
