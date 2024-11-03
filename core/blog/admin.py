from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date', 'category')
    list_filter = ('status', 'created_date', 'published_date', 'category')
    search_fields = ('title', 'content')
    ordering = ('published_date',)
    date_hierarchy = 'published_date'
    raw_id_fields = ('category',)  # اضافه کردن این خط برای انتخاب آسان‌تر دسته‌بندی‌ها

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('num',)
