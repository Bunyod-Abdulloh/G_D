from django.contrib import admin
from .models import User, Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8, Table9, Table10, Tables


class CommonAdmin(admin.ModelAdmin):
    list_display = ('lesson_number', 'file_name', 'caption')
    ordering = ('lesson_number',)
    list_filter = ('file_name',)
    search_fields = ('file_name',)


class CommonAdminTwo(admin.ModelAdmin):
    list_display = ('table_number', 'table_name', 'files')
    ordering = ('table_number',)


class Table10Admin(admin.ModelAdmin):
    list_display = ('articles_number', 'file_name')
    ordering = ('articles_number',)


tables = [Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8]

for table in tables:
    admin.site.register(table, CommonAdmin)

admin.site.register(Table9, CommonAdmin)
admin.site.register(Table10, Table10Admin)
admin.site.register(Tables, CommonAdminTwo)
admin.site.register(User)
