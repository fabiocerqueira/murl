#-*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import redirect

from murl.models import MUrl


def redirect_url(request, murl):
    try:
        m = MUrl.objects.get(murl=murl)
        m.click(True)
        return redirect(m.url)
    except MUrl.DoesNotExist:
        raise Http404()
