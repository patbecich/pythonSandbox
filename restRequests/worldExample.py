import psycopg2

print psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="YellowDog",
    host="127.0.0.1",
    port="5433"
    )

print conn


cur = conn.cursor()
foo = 'true'

print "=========="
cur.execute('SELECT * FROM country;')

while foo: 
    foo = cur.fetchone()
    print foo

conn.commit()

cur.close()

conn.close()

print 'Cursor and connection closed'
