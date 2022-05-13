# Bookstore
How to run the application

Clone the repository from github
`git clone https://github.com/collinskoech/Bookstore.git`

install python3 & pip
`sudo apt-get install python3`

install virtualenv
`pip install virtualenv`

create a virtual environment inside the root folder of the project
`virtualenv env`

activate the virtual environment
`source env/bin/activate`

install the dependencies listed in requirements.txt
`pip install -r requirements.txt`

run database migrations
`python manage.py makemigrations && python manage.py migrate`

create a superuser account
`python manage.py createsuperuser`



## How to access the endpoints

run the sever
`poython manage.py runserver`

## Database design 

### Book Table
| Field name | Data Type | 
| :-- | :-- | 
| [title] | [CharField(200)] | 
| [Author] | [ForeignKey(AuthorId)] | 
| [year] | [IntegerField] | 
| [description] | [CharField(200)] | 
| [quantity] | [IntegerField] | 


### Author Table
| Field name | Data Type | 
| :-- | :-- | 
| [fname] | [CharField(200)] | 
| [lname] | [CharKey(AuthorId)] | 
| [email] | [CharField] | 
| [Date_of_birth] | [DateField] | 



