# Bookstore

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


## How to run the Bookstore server 

![clone from github](./resources/gitclone.png "Title")

![install python](./resources/installpython.png "Title")


![install virtualenv](./resources/installvirtualenv.png "Title")


![create virtual environment](./resources/createvirtualenv.png "Title")


![activate virtualenv](./resources/activatevirtualenv.png "Title")


![install dependencies](./resources/installdependencies.png "Title")


![db migrations](./resources/dbmigrations.png "Title")


![create superuser](./resources/createsuperuser.png "Title")



## How to access the endpoints

run the sever
`poython manage.py runserver`





