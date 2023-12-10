from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)
    # bcrypt.init_app(app)

# DEFAULT_POSTER = '/images/image_not_found/poster_not_found'

# MODELS GO BELOW
# Assiociation table for user fav
# user_favorites = db.Table('user_favorites',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
#     db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
# )


# class UserFav(db.Model):
#     """user fav movie tabke"""

#     __tablename__ = "user_fav"

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
#     db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'))

#     movies = db.relationship('Movie', backref=db.backref('user_fav', lazy=True))
#     users = db.relationship('User', backref=db.backref('user_fav', lazy=True))

#     @classmethod
#     def insert(user_id, movie_id):
#         """"""
#         user_fav = UserFav(user_id=user_id, movie_id=movie_id)
#         db.session.add(user_fav)
#         db.session.commit()

    #      @classmethod
    # def register(cls, username, pwd):
    #     """Register user w/hashed password & return user."""

    #     hashed = bcrypt.generate_password_hash(pwd)
    #     # turn bytestring into normal (unicode utf8) string
    #     hashed_utf8 = hashed.decode("utf8")

    #     # return instance of user w/username and hashed pwd
    #     return cls(username=username, password=hashed_utf8)

# stars = db.relationship('Star', secondary=stars_movies, lazy='subquery', backref=db.backref('movies', lazy=True))



class User(db.Model):
    """tables for users"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False,  unique=True)
    password = db.Column(db.Text, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Self-referencing foreign key
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))  # Foreign key to movies table


    # Relationship to self
    children = db.relationship('User')

    # Relationship to Movie
    # favorite_movie = db.relationship('Movie', backref='users')
    # favorites = db.relationship('UserFav', backref='users', lazy=True)

    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8)

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False



##### Association tables fro many-to-many relationships #####
stars_movies = db.Table('stars_movies',
    db.Column('star_id', db.Integer, db.ForeignKey('stars.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)

directors_movies = db.Table('directors_movies',
    db.Column('director_id', db.Integer, db.ForeignKey('directors.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)

producers_movies = db.Table('producers_movies',
    db.Column('producer_id', db.Integer, db.ForeignKey('producers.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)

writers_movies = db.Table('writers_movies',
    db.Column('writer_id', db.Integer, db.ForeignKey('writers.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)


class Movie(db.Model):
    """All about movies go here:
    Name, genre, stars, director, producer, writer, studio, relese_date, rated, runtime, plot, poster_img"""

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False) # ForeignKey ref for genre
    release_id = db.Column(db.Integer, db.ForeignKey('release_dates.id'), nullable=False)  # Correct foreign key
    rated_id = db.Column(db.Integer, db.ForeignKey('ratings.id'), nullable=False)
    runtime_id = db.Column(db.Integer, db.ForeignKey('runtimes.id'), nullable=False)
    plot_id = db.Column(db.Integer, db.ForeignKey('plots.id'), nullable=False)
    stars_id = db.Column(db.Integer, nullable=False)
    director_id = db.Column(db.Integer, nullable=False)
    producer_id = db.Column(db.Integer, nullable=False)
    writer_id = db.Column(db.Integer, nullable=False)
    studio_id = db.Column(db.Integer, nullable=False)
    poster_img_id = db.Column(db.Integer, db.ForeignKey('posters.id'), nullable=False)

    stars = db.relationship('Star', secondary=stars_movies, lazy='subquery', backref=db.backref('movies', lazy=True))
    directors = db.relationship('Director', secondary=directors_movies, lazy='subquery', backref=db.backref('movies', lazy=True))
    producers = db.relationship('Producer', secondary=producers_movies, lazy='subquery', backref=db.backref('movies', lazy=True))
    writers = db.relationship('Writer', secondary=writers_movies, lazy='subquery', backref=db.backref('movies', lazy=True))
    genre = db.relationship('Genre', backref='associated_movies', lazy=True)
    release_date = db.relationship('Release', lazy=True)
    rated = db.relationship('Rated', lazy=True)
    runtime = db.relationship('Runtime', lazy=True)
    plot = db.relationship('Plot', lazy=True)
    poster = db.relationship('Poster', uselist=False, lazy=True)


class Star(db.Model):
    """List of all actors/actresses"""

    __tablename__ = 'stars'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    dob = db.Column(db.Text, nullable=False)
    bio = db.Column(db.Text, nullable=False)

class Director(db.Model):
    """List of all directors"""

    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    dob = db.Column(db.Text, nullable=False)
    bio = db.Column(db.Text, nullable=False)

class Producer(db.Model):
    """List of all producers"""

    __tablename__ = 'producers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    dob = db.Column(db.Text, nullable=False)
    bio = db.Column(db.Text, nullable=False)

class Writer(db.Model):
    """List of all writers"""

    __tablename__ = 'writers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    dob = db.Column(db.Text, nullable=False)
    bio = db.Column(db.Text, nullable=False)

class Studio(db.Model):
    """Studios that made the movie"""

    __tablename__ = 'studios'

    id = db.Column(db.Integer, primary_key=True)
    studio_name = db.Column(db.Text, nullable=False)
    studio_est_date = db.Column(db.Date, nullable=False)
    

class Poster(db.Model):
    """table for movie posters"""

    __tablename__ = 'posters'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.Text, nullable=False)
    

class Genre(db.Model):
    """movie genre"""

    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.Text, nullable=False)

    # Relationship backref from Movie
    movies = db.relationship('Movie')
    
class Release(db.Model):
    "Relese date in mm/dd/year formate"

    __tablename__ = 'release_dates'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)

    movies = db.relationship('Movie')

class Rated(db.Model):
    """Rating for movie like: R, PG13, MA, TV-MA, etc"""

    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    rated = db.Column(db.Text, nullable=False)

    # Relationship backref from Movie (optional, only if you need to access movies directly from a Rated object)
    movies = db.relationship('Movie')

class Runtime(db.Model):
    """Movie tuntime in hr:min:sec formate"""

    __tablename__ = 'runtimes'

    id = db.Column(db.Integer, primary_key=True)
    hour = db.Column(db.Integer, nullable=False)
    minutes = db.Column(db.Integer, nullable=False)
    seconds = db.Column(db.Integer, nullable=False)

class Plot(db.Model):
    """brief synopsis of the movies"""

    __tablename__ = 'plots'

    id = db.Column(db.Integer, primary_key=True)
    plot = db.Column(db.Text, nullable=False)


# class UserFav(db.Model)

# Review table
class Review(db.Model):
    """Saves reviews written by users"""

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text)