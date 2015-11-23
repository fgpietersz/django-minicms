# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, unicode_literals)

from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from admirarchy.toolbox import HierarchicalModelAdmin

from .models import Page


class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ()
        widgets = {
            'content': CKEditorUploadingWidget(config_name='minicms')}


class PageAdmin(HierarchicalModelAdmin):
    hierarchy = True
    form = PageAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('list_title', 'position', 'slug')
    ordering = ('position',)

    def list_title(self, page):
        return ' ⇒ '.join([p.title for p in (list(page.ancestors()) + [page])])

admin.site.register(Page, PageAdmin)
