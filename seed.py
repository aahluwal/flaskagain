import model
import csv
import re #regex to remove year from title
import datetime

# read each row in, parse it, 
# then insert it into the database using our SQLAlchemy object interface.
# open a file
# read a line
# parse a line
# create an object
# add the object to a session
# commit
# repeat until done

def load_users(session):
    # use u.user
    #open the user file
    with open("seed_data/u.user") as f:
        #read from database, seperate items by |
        reader = csv.reader(f, delimiter="|")
        #iterate through the database line by line
        for row in reader:
            #assign an id to each field
            id, age, gender, occupation, zipcode = row 
            id = int(id)
            age = int(age)
            #set up model to be added to db
            u = model.User(id=id, age=age, zipcode=zipcode)
            #add changes to db
            session.add(u)
        #commit changes to the db
        session.commit()
def load_movies(session):
    # use u.item
    with open("seed_data/u.item") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            id = row[0]
            name_1 = row[1]
             #regex to remove date in () from title field from variable name
            name_2 = re.sub("\(\d{4}\)", "", name_1) 
            name = name_2.decode("latin-1")
            released_at = row[2]
            if not released_at:
                continue
            #datetime is a method within a class called datetime. 
            #Strptime is a method of datetime class also 
            released_at = datetime.datetime.strptime(row[2], '%d-%b-%Y')
            imdb_url = row[4] 
            m = model.Movie(id = id, name = name, released_at= released_at, 
                imdb_url= imdb_url)    
            session.add(m) 

        session.commit()

def load_ratings(session):
    # use u.data
    #user_id     movie_id     rating     timestamp
    with open("seed_data/u.data") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            user_id = row[0]
            movie_id = row[1]
            rating = row[2]
            timestamp = row[3]
            d = model.Rating(user_id = user_id, movie_id = movie_id, rating = rating)
            session.add(d)
        session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_movies(session)
    load_users(session)
    load_ratings(session)

if __name__ == "__main__":
    s = model.connect()
    main(s)
