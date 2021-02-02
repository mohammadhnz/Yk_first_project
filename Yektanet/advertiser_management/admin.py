from django.contrib import admin

from .models import Advertiser, Ad, Click, View


class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'advertiser', 'link', 'id', 'approve', 'views')
    list_filter = ('advertiser_id', 'approve')
    search_fields = ('title',)
    ordering = ['approve']


admin.site.register(Ad, AdAdmin)
admin.site.register(Advertiser)
admin.site.register(Click)
admin.site.register(View)
# Register your models here.
