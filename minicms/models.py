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
    position = models.PositiveIntegerField(default=1000)
    parent = models.ForeignKey('self', related_name='children',
        null=True, blank=True, db_index=True)
    urlpath = models.CharField(max_length=1000, editable=False, unique=True)

    class Meta:
        unique_together = ('slug','parent')
        ordering = ('position',)

    def __str__(self):
        return self.urlpath + '  ' + self.title

    def get_absolute_url(self):
        return reverse('page', args=[self.urlpath])

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

    def siblings(self):
        if not (hasattr(self, '_siblings') and self._siblings):
            self._siblings = Page.objects.filter(parent=self.parent)
        return self._siblings

    def ancestors(self):
        if self.parent is None:
            return []
        if hasattr(self, '_ancestors') and self._ancestors:
            return self._ancestors
        path_list = None
        for i in self.urlpath.split('/')[:-1]:
            if path_list:
                path_list.append('/'.join((path_list[-1], i)))
            else:
                path_list = [i]
        self._ancestors = Page.objects.filter(
                urlpath__in=path_list).order_by('urlpath')
        return self._ancestors
