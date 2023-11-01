from django.contrib import admin


class WorkAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Type')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('Title',)
