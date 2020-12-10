# PWA2020
Programowanie aplikacji webowych 2020

## Autor
### Niedzielski 206074

## Soft:
* WEB: Django 3
* DB: sqlite3
* PYTHON: python3
* JS: jquery/jquery-ui
* CMS: bootstrap4

## Run:
~~~
git clone https://github.com/Marynarz/PWA2020.git
cd PWA2020/pwa_project
python3 manage.py makemigrations tablice_main
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver
~~~

## URLS:
url | description
--- | -----------
 | start page
logout/ | logout
index/ | user main page
board/<int:board_id>/ | board with id <board_id>
operation | adding board
operation/<int:board_id> | adding tab or removing board
operation/<int:board_id>/<int:tab_id> | adding element or removing tab
operation/<int:board_id>/<int:tab_id>/<int:elem_id> | removing tab
position/tab/<int:board_id> | setting tab position on board
position/elem/ | setting element position on board