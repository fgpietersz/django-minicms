# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, unicode_literals)

from django.db import models
from django.db import transaction
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=50)
    published = models.BooleanField(default=True)
    position = models.PositiveIntegerField(default=1000)
    parent = models.ForeignKey('self', related_name='children',
                               null=True, blank=True, db_index=True)
    urlpath = models.CharField(max_length=1000, editable=False, unique=True)

    _siblings = None
    _ancestors = None
    _child_pages = None

    class Meta:
        unique_together = ('slug', 'parent')
        ordering = ('position',)

    def __str__(self):
        return self.urlpath + ': ' + self.title

    def get_absolute_url(self):
        return (reverse('minicms:page', args=[self.urlpath])
                if self.urlpath else
                reverse('minicms:home'))

    def save(self, *args, **kwargs):
        if not kwargs.get('commit', False):
            super(Page, self).save(*args, **kwargs)
        with transaction.atomic():
            if self.parent:
                self.urlpath = '%s/%s' % (self.parent.urlpath, self.slug)
            else:
                self.urlpath = self.slug
            for child in self.children.all():
                child.save()
            super(Page, self).save(*args, **kwargs)

    def clear_cached_props(self):
        self._siblings = None
        self._ancestors = None
        self._child_pages = None

    def siblings(self):
        if self._siblings is None:
            self._siblings = Page.objects.filter(
                parent=self.parent, published=True)
        return self._siblings

    def child_pages(self):
        self.children.filter(published=True)

    def ancestors(self):
        """Get ancestors"""
        if self._ancestors is not None:
            return self._ancestors
        if self.parent is None:
            self._ancestors = []
        else:
            path_list = None
            for i in self.urlpath.split('/')[:-1]:
                if path_list:
                    path_list.append('/'.join((path_list[-1], i)))
                else:
                    path_list = [i]
            self._ancestors = Page.objects.filter(
                urlpath__in=path_list).order_by('urlpath')
        return self._ancestors
