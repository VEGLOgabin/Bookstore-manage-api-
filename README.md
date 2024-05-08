# Bookstore-manage-api
BACKEND API FOR BOOKSTORE NAMAGE


################################################################################################################################
       THIS IS AN API FOR MANAGE BOOKSTORE

################################################################################################################################

###############################################
FUNCTIONALITIES OF THIS API
###############################################

This api have many advantages for all bookstore manage project.

-In this api , you have three types of user:  books borrowers or simple users, books managers users , admins users
-The admin have the responsability:  create book manager user profil
-The books managers users have the responsabilities to create book category, add book, delete book, validate commanded book, delete validated book after returned
-users or all users:  command the borrowing book, post massage or feed-back,comment a post , like a post





#############################################
      RUN THIS API ON YOU COMPUTER
#############################################

-If you want to compile this api in local or use it for everythings in your project , you need to clone it  by runing this command in your linux shell:   git clone "link from github repository".
- you need to have python(version >=3.7) installed on your computer
- move in the project directory by runing this command:  cd backend
- now create a virtual environnement by runing this command:  python -m venv 'your virtual env name here'
- install all package by runing this command :  pip install -r requirements.txt
- make migration by runing:  python manage.py makemigrations & python manage.py migrate
- start the server by runing:  python manage.py runserver
- so you can find the documentation of api at 127.0.0.1:8000/redoc 
- you can also find the swagger at 127.0.0.1:8000/swagger



