
from django.contrib import admin
from .models import Paragraph

@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
	list_display = ('id', 'text', 'created_at')
