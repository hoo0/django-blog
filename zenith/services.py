from django.conf import settings
import time
import requests
import urllib

from .app_exception import AppException

ZENITH_DOMAIN = settings.ZENITH_DOMAIN

class Services:
    
    @staticmethod
    def make_url(request, service):
        url = ZENITH_DOMAIN + settings.ZENITH_URL[service]
        headers = {'Accept': 'application/json'}
        params = {
            'timestamp': str(time.time()),
        }
        # params['uid'] = '0010203806'

        if service != 'login':
            if 'uid' not in params or params['uid'] == '':
                if 'uid' not in request.session or request.session['uid'] == '':
                    raise AppException('session-expired', 'session expired')

                params['uid'] = request.session['uid']

        print('url={} params={}'.format(url, params))

        return url, headers, params

    @staticmethod
    def login(request, id, password):
        url, headers, params = Services.make_url(request, 'login')
        params['loginID'] = id
        params['password'] = password
        r = requests.get(url, headers=headers, params=params, timeout=2.0)

        if r.status_code == 200:
            data = r.json()
            print(data)
            
            if data['result'] == 'OK':
                request.session['uid'] = data['uid']
                
            return data
        else:
            raise AppException(r.status_code, 'login_error', 'login error')

    @staticmethod
    def list(request):
        url, headers, params = Services.make_url(request, 'control')
        params['type'] = 'list'

        r = requests.get(url, headers=headers, params=params, timeout=2.0)

        if r.status_code == 200:
            data = r.json()
            return data
        else:
            raise AppException(r.status_code, 'error', 'error')


    @staticmethod
    def status(request, type, code):
        url, headers, params = Services.make_url(request, 'control')
        params['type'] = type
        params['code'] = code
        params['cmd'] = 'get'

        r = requests.get(url, headers=headers, params=params, timeout=2.0)

        if r.status_code == 200:
            data = r.json()
            return data
        else:
            raise AppException(r.status_code, 'error', 'error')

    @staticmethod
    def proxy(request):
        headers = {'Accept': 'application/json',
                  'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        path = request.GET.get('path')
        method = request.GET.get('method')
        # print('request.GET.dict()=', request.GET.dict())
        
        path = urllib.parse.unquote(path)
        print('path=', path)
        params = request.GET.dict()
        # params['sid'] = urllib.parse.quote(params['sid'])
        del params['path']
        print('params=', params)

        r = requests.post(path, headers=headers, params=params, timeout=5.0)

        if r.status_code == 200:
            data = r.json()
            return data
        else:
            raise AppException(r.status_code, 'error', 'error')

    @staticmethod
    def proxy_get(request):
        headers = {'Accept': 'application/json',
                  'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        path = request.GET.get('path')
        
        path = urllib.parse.unquote(path)
        print('path=' + path)

        r = requests.get(path, headers=headers, timeout=5.0)

        if r.status_code == 200:
            data = r.json()
            return data
        else:
            raise AppException(r.status_code, 'error', 'error')

    @staticmethod
    def proxy_post(request):
        headers = {'Accept': 'application/json',
                  'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        path = request.GET.get('path')
        # print('request.GET.dict()=', request.GET.dict())
        
        path = urllib.parse.unquote(path)
        print('path=', path)
        params = request.GET.dict()
        # params['sid'] = urllib.parse.quote(params['sid'])
        del params['path']
        print('params=', params)

        r = requests.post(path, headers=headers, params=params, timeout=5.0)

        if r.status_code == 200:
            data = r.json()
            return data
        else:
            raise AppException(r.status_code, 'error', 'error')
