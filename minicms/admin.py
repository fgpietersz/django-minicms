# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, unicode_literals)

from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Page


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ()
        widgets = {
            'content': CKEditorUploadingWidget(config_name='minicms')}


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('urlpath', 'title', 'slug')

admin.site.register(Page, PageAdmin)
