from sqlalchemy import create_engine, Table, Column, String, MetaData, Integer

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('Login', String, nullable=False),
              Column('Hash_Password', String, nullable=False),
              Column('Score', Integer, default=0))

engine = create_engine('sqlite:///users.db', echo=True)
metadata.create_all(engine)
conn = engine.connect()

