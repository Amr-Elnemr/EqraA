# EqraA

A Simple book reviewing system

## Prerequisites (Used Technologies)

* Python v3.4 or above
* Django v2.0
* MySQL database engine 


## Installing

1- Create a database and name it 'EqraA'

2- In the project folder run:
```
		python3 manage.py makemigrations library
		python3 manage.py migrate
		python3 manage.py runserver
```
3- Start the app in your browser via this url:
```
		http://localhost:8000/library/register/
```
4- To Start adding Authors, Books, and Genres:
a) create a super-user (by running this command in the project folder):
```
		python3 manage.py createsuperuser
```
	
b) login to admin page:

```
		http://localhost:8000/admin/
```
## Authors

* Ahmed Essam [ahmed-essam](https://github.com/ahmed-essam)
* Amr Essam [Amr-Elnemr](https://github.com/Amr-Elnemr)
* George Samir [georgesamir21](https://github.com/georgesamir21)
* Mohamed Omran [mohamedgomran](https://github.com/mohamedgomran) 
