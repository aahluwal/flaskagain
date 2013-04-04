from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref


ENGINE = None
Session = None

ENGINE = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit=False, autoflush=False))

Base = declarative_base()

### Class declarations go here

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key = True)
	email = Column(String(64), nullable = True)
	password = Column(String(64), nullable = True)
	age = Column(Integer, nullable= True)
	zipcode = Column(String(15), nullable = True)

	def __repr__(self):
		return ("User: %d, %s, %s, %d, %s") % (self.id, self.email, self.password, self.age, self.zipcode)
	 


class Movie(Base):
	__tablename__= "movies"

	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable = False)
	released_at = Column(Date, nullable = False)
	imdb_url = Column(String(128), nullable = False)

	def __repr__(self):
		return ("Movie: %d, %s, %r, %s")% (self.id, self.name, self.released_at, self.imdb_url)

class Rating(Base):
	__tablename__= "ratings"

	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey("users.id"))
	movie_id = Column(Integer, ForeignKey("movies.id"))
	rating = Column(Integer, nullable = False)

	#create a relation between movie, user and ratins
	user = relationship("User",
		backref=backref("ratings", order_by=id))
	movie = relationship("Movie", backref=backref("ratings", order_by=id))
	#represent function that prints out object
	def __repr__(self):
		return("Rating: %d, %d, %d, %d") % (self.id, self.user_id, self.movie_id, self.rating)


	
### End class declarations

# def connect():
# 	global ENGINE
# 	global Session



# 	return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
