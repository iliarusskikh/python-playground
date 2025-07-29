#Using SQLAlchemy Core with SQLite

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select

# Create engine
engine = create_engine('sqlite:///example.db', echo=True)# echo=True logs SQL queries

# Define metadata
metadata = MetaData()

# Define a table
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String, nullable=False),
              Column('age', Integer))

# Create the table
metadata.create_all(engine)

# Insert data
with engine.connect() as conn:
    conn.execute(users.insert().values(name="Bob", age=30))
    conn.commit()
    conn.execute(users.insert().values(name="Sola", age=22))
    conn.commit()
    conn.execute(users.insert().values(name="Kale", age=44))
    conn.commit()

# Query data
with engine.connect() as conn:
    result = conn.execute(select(users).where(users.c.age > 25))
    for row in result:
        print(row)
        
#def main():
#    print("Hello from sqlalch!")
#
#if __name__ == "__main__":
#    main()
