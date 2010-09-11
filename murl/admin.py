# -*- coding: utf-8 -*-
from django.contrib import admin

from murl.models import MUrl

class MUrlAdmin(admin.ModelAdmin):
    list_display = ('murl','url','owner', 'publication', 'clicks')
    search_fields = ['url','murl']
    list_filter = ['publication']

admin.site.register(MUrl, MUrlAdmin)
