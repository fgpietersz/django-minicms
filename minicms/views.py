# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, unicode_literals)

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.conf import settings

from .models import Page


def page_view(request, urlpath):
    page = get_object_or_404(Page.objects.select_related('parent'),
        urlpath=urlpath, published=True)
    ancestors = page.ancestors()
    if any(a.published == False for a in ancestors):
        raise Http404
    tmpls = ['minicms.html']
    tmplpath = 'minicms'
    for slug in urlpath.split('/'):
        tmplpath = tmplpath + '/' + slug
        tmpls.append(tmplpath + '.html')
    tmpls.reverse()
    return render(request, tmpls, {'page': page, 'ancestors': ancestors})


def home_page(request):
    return page_view(request, settings.HOME_PAGE_PATH)