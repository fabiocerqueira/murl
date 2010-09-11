#-*- coding: utf-8 -*-
import urllib2
import urllib
import simplejson as json
from pprint import pprint

REALM = 'MyUrl'
BASE_URL = 'http://localhost:8000/api/'

class HTTPRequest(urllib2.Request):
    """Hack urllib2.Request to support PUT and DELETE methods."""
 
    def __init__(self, url, method="GET", data=None, headers={},
                 origin_req_host=None, unverifiable=False):
        urllib2.Request.__init__(self,url,data,headers,origin_req_host,unverifiable)
        self.url = url
        self.method = method
 
    def get_method(self):
        return self.method

class MUrlApi(object):
    def __init__(self, user, passwd):
        self.auth_handler = urllib2.HTTPBasicAuthHandler()
        self.auth_handler.add_password(realm=REALM,uri=BASE_URL, user=user, passwd=passwd)
        self.opener = urllib2.build_opener(self.auth_handler)
        urllib2.install_opener(self.opener)


    def get_urls(self):
        text = urllib2.urlopen(BASE_URL + 'urls').read()
        return json.loads(text)

    def get_url(self, murl):
        text = urllib2.urlopen(BASE_URL + 'url/' + murl).read()
        return json.loads(text)

    def delete_url(self, murl):
        try:
            req_data = HTTPRequest(BASE_URL + 'url/' + murl, 'DELETE')
            req = urllib2.urlopen(req_data)
            return req.code == 200
        except urllib2.HTTPError as e:
            return False

    def create_url(self, murl, url):
        try:
            data = urllib.urlencode({'url':url})
            req_data = HTTPRequest(BASE_URL + 'url/' + murl, 'POST', data)
            req = urllib2.urlopen(req_data)
            return json.loads(req.read())
        except urllib2.HTTPError as e:
            return None



def main():
    c = MUrlApi('fabio','1234')
    print "Add new murl:"
    new_murl = c.create_url('pugce','http://pug-ce.python.org.br')
    pprint(new_murl)
    print '-' * 50,'\n'

    print 'All murls'
    all_url = c.get_urls()
    pprint(all_url)
    print '-' * 50,'\n'

    print 'Info last murl'
    murl = all_url[0]['murl']
    info_murl = c.get_url(murl)
    pprint(info_murl)
    print '-' * 50,'\n'

    print 'Del last murl'
    print c.delete_url(murl)
    

if __name__ == '__main__':
    main()


