#-*- coding: utf-8 -*-
from piston.handler import BaseHandler
from piston.utils import rc
from murl.models import MUrl

class MUrlHandler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'DELETE')
    model = MUrl   
    fields = ('murl', 'url', 'publication', 'clicks')

    def read(self, request, murl=None): 
        """
        Retorna detalhe de um uma murl ou todas as urls

        Parâmetros:
         - murl: slug para murl que deseja ver detalhes
        """
        if not murl:
            return MUrl.objects.filter(owner=request.user)
            
        try:
            return MUrl.objects.get(murl=murl, owner=request.user)
        except MUrl.DoesNotExist:
            return rc.NOT_FOUND

    def create(self, request, murl):
        """
        Cria uma nova murl

        Parâmetros:
         - murl: slug com o nome para nova url 
        """
        try:
            m = MUrl.objects.get(murl=murl, owner=request.user)
            return rc.DUPLICATE_ENTRY
        except MUrl.DoesNotExist:
            attrs = self.flatten_dict(request.POST)
            murl = MUrl(murl=murl, url=attrs['url'], owner=request.user)
            murl.save()
            return murl


    def delete(self, request, murl):
        """
        Remove uma murl

        Parâmetros:
         - murl: slug com o nome da murl para remover 
        """
        try:
            m = MUrl.objects.get(murl=murl, owner=request.user)
            m.delete()
            return rc.ALL_OK
        except MUrl.DoesNotExist:
            return rc.NOT_FOUND

        
