#Using SQLAlchemy ORM with SQLite
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a SQLite database (file-based)
engine = create_engine('sqlite:///example.db', echo=True)  # echo=True logs SQL queries

# Define a base class for ORM models
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

# Create the table
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
new_user = User(name="Bob", age=25)
session.add(new_user)
session.commit()

new_user = User(name="Josh", age=32)
session.add(new_user)
session.commit()

# Query data
users = session.query(User).filter_by(age=25).all()
for user in users:
    print(user.name, user.age)  # Output: Bob 25

# Close the session
session.close()



#def main():
#    print("Hello from sqlalch!")
#
#if __name__ == "__main__":
#    main()
