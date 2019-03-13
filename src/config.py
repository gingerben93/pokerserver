import os

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

print("test")
print(user)
print(port)

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
#DATABASE_CONNECTION_URI = 'postgresql+psycopg2://' + user + ':' + password + '@' + host + ':' + port + '/' + database
