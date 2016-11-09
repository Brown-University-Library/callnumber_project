# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Subject
from django.contrib import admin


class SubjectAdmin( admin.ModelAdmin ):
    list_display = ( 'name', 'code_range', 'note' )
    search_fields = ( 'id', 'name', 'code_range', 'note' )


admin.site.register(Subject, SubjectAdmin)
