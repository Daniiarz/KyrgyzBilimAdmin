from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.SubTopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic_name')
    search_fields = ('text', )
    list_filter = ('topic',)

    def topic_name(self, obj):
        return obj.topic.name


admin.site.register(models.Course)
admin.site.register(models.Section)
admin.site.register(models.Topic)
