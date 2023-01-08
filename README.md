```
┌───────────────────────────────────────────────┐
                                       _       
     __ _  ___   ___  _ __ _ __ ___   (_) ___  
    / _` |/ _ \ / _ \| '__| '_ ` _ \  | |/ _ \ 
   | (_| | (_) | (_) | |  | | | | | |_| | (_) |
    \__, |\___/ \___/|_|  |_| |_| |_(_)_|\___/ 
    |___/                                      
			     🌩 𝘼𝙣𝙮𝙤𝙣𝙚 𝙘𝙖𝙣 𝙙𝙚𝙫𝙚𝙡𝙤𝙥!
└───────────────────────────────────────────────┘
```

# django
장고 공부하기

goormIDE is a powerful cloud IDE service to maximize productivity for developers and teams.  
**DEVELOP WITH EXCELLENCE**  

`Happy coding! The goormIDE team`

* todo
	* 배포체계 - github or
	* 서버구성 - nginx, venv, supervisor/systemd, wsgi


## 🔧 Tip & Guide

* settings변경사항 반영
    * python manage.py migrate

* app 만들기
	* python manage.py startapp blog

* db. 새 모델 테이블 생성
	* python manage.py makemigrations blog
	* python manage.py migrate blog

* 관리자. superuser 생성
	* python manage.py createsuperuser

* 관리자 패널에 Comment 모델 등록
    * @ blog/admin.py
    * admin.site.register(Comment)

* 서버기동
    * python manage.py runserver

* DRF(Django Rest Freamework) CORS policy
    * pip install django-cors-headers
    * settings.py
        ** INSTALLED_APPS - corsheaders
        ** MIDDLEWARE - 맨위 corsheaders.middleware.CorsMiddleware
        ** CORS_ORIGIN_ALLOW_ALL = True
        ** CORS_ALLOW_CREDENTIALS = True

