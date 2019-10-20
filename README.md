# django-blog

a simple blog app in django 


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)


## General Info
This repository is a very simple weblog app written in **Python3/Django**.Although this is a basic form of a weblog but it supports the regular features of a blog app such as Authentication and Authorization system(log the user in , log him out ,etc) using the django session framework and CRUD proccess(create,read,update and delete).
The project has running on this link for online testing  http://vahid75.pythonanywhere.com/chat/login 

---

## Technologies
* **Python 3**
* **Django 2.2**
* **Bootstrap 4**

---

## Setup



If you want to run this app in your Django project , follow [add to your project](#add-to-your-project) or for run it in a blank project go to [build a project](#build-a-project)



#### add to your project

- download the ```chat```  directory in your project folder.

- add app to your project settings.py ```chat.apps.ChatConfig)``` and add these to your root ```urlconf```:

  ```path('chat/', include('chat.urls'))```



#### build a project

- making a virtualenv named venv using 

  ```virtualenv venv ```
  
- activate it using this step in UNIX os family

  ```source venv/bin/activate```
  
- or

  ```cd venv/bin/; ./activate```
  
- install django 

  ```pip3 install Django==2.2.3```

- now clone the whole repository.
- for UNIX systems in terminal type

  ```./manage.py runserver```
  
- or in WINDOWS type in console 

  ```py manage.py runserver```
  
- open the http://127.0.0.1:8000/ in your browser
