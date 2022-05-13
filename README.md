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


