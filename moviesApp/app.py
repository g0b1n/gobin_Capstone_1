from flask import Flask, request, render_template, redirect, flash, url_for, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Movie, Star, Director, Producer, Writer, Studio, Genre, Release, Rated, Runtime, Plot, Poster, Review
# Import association tables if needed
# from models import stars_movies, directors_movies, producers_movies, writers_movies
from forms import CreateAccountForm, LoginForm, ReviewForm
from sqlalchemy.exc import IntegrityError
import requests
from api_calls import fetch_movie_data, trendingMvi, trendingPerson, get_movie_details, get_movie_cast, person_details, get_known_for, get_movie_reviews
from secrets_1 import apiKey

# My API key
api_key = apiKey


app = Flask(__name__)
# db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'movieRatingApp'
# debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///myMvi_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# db.init_app(app)

connect_db(app)

def setup_database(app):
    with app.app_context():
        db.create_all()

"""
I will need a route where I can display player information. This route can only be accessed by searching players name in the search bar.
If a user tries to go directly to this page it will redirect them to the home page
"""

def get_trending_person(query):
    """Show trending person"""
    trending_person = trendingPerson(query)
    return trending_person


@app.route('/')
def home_page():
    """
    Landing page showing current popular movies, TV shows, and series.
    """
    query = request.args.get('query', '') 
    trending_data = trendingMvi(query)
    trending_person = get_trending_person(query)
    if trending_data and trending_person:
        return render_template('home.html', trending_items=trending_data['results'],
                                trending_person=trending_person['results'])
    else:
        return render_template('home.html', error="No data found")




@app.route('/login', methods=['GET', 'POST'])
def login_user():
    """Renders and handles form to login"""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            flash(f"Welcome Back, { user.username }", 'primary')
            session['user_id'] = user.id
            session['username'] = user.username #stores username in session
            return redirect('/')
        else:
            form.username.errors = ["Invalid credentials, please try again"]

    return render_template('login.html', form=form)


# CREATE ACCOUNT
@app.route('/create-account', methods=['GET', 'POST'])
def create_acc():
    """Renders and handles the form to create a new account"""
    form = CreateAccountForm()
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = form.password.data

        new_user = User.register(username, password)

        db.session.add(new_user)
        # duplicate user error
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username already exist, please choose another username!!!')
            return render_template('create-acc.html', form=form)
        
        session['user_id'] = new_user.id

        flash('Welcome! Successfully Created Your Account!!', 'success')
        return render_template('/') #show the list of their movies after LOGING IN

    return render_template('create-acc.html', form=form)


# LOGOUT
@app.route('/logout')
def logout_user():
    session.pop('user_id', None)
    session.pop('username', None) #Remove username form session
    flash("Successfully logged out", 'info')
    return redirect('/')

@app.route('/username')
def adding_userPic():
    return render_template('username.html')

if __name__ == '__main__':
    setup_database(app)
    app.run(debug=True)


##### TRYING THE API ##### 

@app.route('/search', methods=['GET', 'POST'])
def search_results():
    """Handles the API search and render templates to append the results to DOM"""

    if request.method == 'POST':
        query = request.form['query']
        movie_data = fetch_movie_data(query, api_key)

        # check if movie_data is not None and has results
        if movie_data and 'results' in movie_data:
            #sort movies by release data (most recent to least recent)
            sorted_movies = sorted(movie_data['results'], key=lambda x: x['release_date'], reverse=True)
            return render_template('search/search_results.html', movies=sorted_movies)
        else:
            flash("No results found", "error")
            return render_template('search/search_results.html')
    
    return render_template('search/search.html')


def movie_cast(movie_id, api_key):
    """Shows the cast of the movie"""
    return get_movie_cast(movie_id, api_key)

def movie_reviews(movie_id, api_key):
    """Shows the reviews of the movie"""
    return get_movie_reviews(movie_id, api_key)

# Get movie details 
@app.route('/movie/<int:movie_id>', methods=['GET', 'POST'])
def movie_details(movie_id):
    """Shows more details about a movie"""

    print("Fetching details for movie ID:", movie_id)
    # Assuming api_key is a global variable that stores your API key
    movie_details = get_movie_details(movie_id, api_key)
    cast_details = movie_cast(movie_id, api_key)
    reviews = movie_reviews(movie_id, api_key)

    if movie_details or movie_cast and reviews:
        return render_template('movies/movie_details.html', movie=movie_details, movie_cast=cast_details['cast'], reviews=reviews['results'])
    else:
        return render_template('movies/movie_details.html', error="Movie details not found.")

# REVIEWS
# @app.route('/reviews', methods=['GET', 'POST'])
# def movie_reviews(movie_id):
#     """shows reviews for a movie"""

#     print("Fetching reviews for movie ID:", movie_id)
#     reviews = get_movie_reviews(movie_id, api_key)

#     if reviews:
#         return render_template('movies/movie_details.html', reviews=reviews['results'])


# Get person details
def known_for(person_id, api_key):
    """Show trending person"""
    person_known_for = get_known_for(person_id, api_key)
    return person_known_for



@app.route('/person/<int:person_id>', methods=["GET", "POST"])
def show_person_details(person_id):
    """Displayes info about celebs"""
    print("Fetching details for movie ID:", person_id)
    details = person_details(person_id, api_key)
    person_known_for = known_for(person_id, api_key)
    # print("Person_known_for:", person_known_for)

    if details and person_known_for:
        return render_template('person.html', person_details=details, person_known_for=person_known_for)
    else:
        error_message = f"Details not found for person ID: {person_id}"
        return render_template('error.html', error=error_message), 404


