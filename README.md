# BooksAndReviews


**Scope**: 
Django application where logged in users can view and add book reviews. A user should also be able to delete his/her own reviews.
 
Implemented multi-page website from scratch (using RESTful routing/Web APIs, MVC, user authentication (login/registration), front and backend validations, backend DB with basic CRUD) Focus was to integrate multiple APIs into project and move the item through front end to back end.

## Environment:
```
Framework : django
Database : MySQL and ORM
Languages : python
CSS Framework : materialiseCSS
```
*It's a small project focusing on Django, database design and accessing session within website. Implemented within 2-3 hours.*

## Features : 

1. User should able to register and login to website sucessfully. 
For incorrect inpute proper user friendly messages/pop-up should get displayed

2. Website Dashboard should consist of:
    * List of recent books reviews 
    * Each review displays book ratings , book name and reviewer details.
    * List of other books ( Books ot added by logged user)
    * User should able to navigate to other users profile or books details.
                      
3. Add a Book : 
    * User should able to add book and its author.
    * Author can be selected from existing populated list or user can add a new author.
    * User should able to provide ratings and review for the book
              
4. Book Details : 
    * User should able to retrive information about book
    * It should consist of book name , author , all the reviews and its rating given by each reviewer.
    * User can add review and ratings for the book
    * User can delete his own review only.
    * Delete option shlould be available for own reviwes
  
 5. User Profile : 
    * Logged in user can see other users profile 
    * It displayes user data (Name , Email etc.) and number of reviwes
    * Also displays list of books where user posted his/her review.
 
 6. User should able to navigate Home/Dashboard or logout anytime.
 
