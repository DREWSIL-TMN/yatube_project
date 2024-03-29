from django.contrib import admin

from .models import Post
from .models import Group


class PostAdmin(admin.ModelAdmin):
    # Возможность корректировки поля group в любом посте
    list_editable = ('group',)
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
