from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author'] #Правое боковое меню фильтрации
    search_fields = ['title', 'body'] #Поля, по которым возможен поиск
    prepopulated_fields = {'slug': ('title',)} #автоматически заполняет поле slug на основе значения поля title.
    raw_id_fields = ['author'] #заменяет стандартное поле выбора (dropdown) для поля author на текстовое поле с возможностью ввода ID.
    date_hierarchy = 'publish' #добавляет навигационную ссылку для фильтрации объектов по дате в верхней части административной панели.
    ordering = ['status', 'publish'] #Сортировка, сначала по статусу, а потом по публикации
