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

![navigate](./resources/navigate.png "Title")

![install python](./resources/installpython.png "Title")


![install virtualenv](./resources/installvirtualenv.png "Title")


![create virtual environment](./resources/createvirtualenv.png "Title")


![activate virtualenv](./resources/activatevirtualenv.png "Title")


![install dependencies](./resources/installdependecies.png "Title")


![db migrations](./resources/dbmigrations.png "Title")


![create superuser](./resources/superuser.png "Title")


## How to access the endpoints

run the sever

![run server](./resources/runserver.png "Title")


### endpoints

get all books

![all books](./resources/books.png "Title")

create a new book

![new books](./resources/newbook.png "Title")

get book with specific id

![specific book](./resources/singlebook.png "Title")

edit book with specific id

![edit book](./resources/Editbook.png "Title")

get books from a specific author

![author specific book](./resources/authorsbook.png "Title")

get books published in a specific year

![books of a specific year](./resources/yearbook.png "Title")

get all authors

![all authors](./resources/authors.png "Title")

get author with specific id

![single authors](./resources/singleauthor.png "Title")

add a new author

![new author](./resources/newauthor.png "Title")

EditAuthor

![edit author](./resources/editauthor.png "Title")

Update stock quantity

![update stock quantity](./resources/updatequantity.png "Title")

