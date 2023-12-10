# gobin_Capstone_1

## **Capstone 1 - myMvi(my Movies DB)**

### **About myMvi**
It's a project/assigment for my course. I am using an api to fetch data and append them in my app. The data I am getting is about
currently trending movies and trending celebrities. I want to add more in future, things like Trending TV shows, Top 10 Movies of the week/month,
popular movies and more. As of now, when you click on the movie or celebrities pictures, it will show you more details about the movie of celebrity you clicked on.
If you click on a movie, it will give you the overview of the movie, list of actors/actress, rating, runtime, genre etc. You can then click on the name/picture of
the actors to get more info about them and the list of other movies that they have worked/known for. You can get more info about actors by clicking on their pictures
from the home page.

I also have a search button on the top, as of now, it only works for movies, I plan to add more features to it to allow it to search form Tv Shows,
celebrities, directors etc. 


### **api_calls.py**
This file has all the api calls that i am making to fetch data from ***TMDB***.

### **models.py**
This file houses all of my ***SQLALchemy Tables*** needed for saving data to my database.
As of now I am only useing a user table to save username and password,
I still have some work to do to make the movies table and other tables work.
It also handles the hash password functions.

### **app.py**
This one has the flask app, all the routes and function/logic to make my app work.
It renders all the templates, verifies if the user is logged in or not. 

### **forms.py**
This file has two of forms to let a user **Create account** and **Login**

## **app.js**
I have one JavaScript file. It does couple of things, it toggles a heart icon inside a button to let users save movies to the favorite.
I still need to figure out a way to make the button connect with my app.py and when a button is clicked and user is logged in it saves that movie to their favorite list.
app.js also handles a function to toggle a dropdown menu, upon click on the username it revels couple of options **My Profile, Favorites Movies and Logout**.
There is still lot of work to be done in this.

### **CSS**
I have some css files but majority of my design is done by using bootstraps.

