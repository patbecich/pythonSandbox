import psycopg2

print psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="YellowDog",
    host="127.0.0.1",
    port="5432"
    )

print conn


cur = conn.cursor()

cur.execute("INSERT INTO foo (num, text) VALUES (%s, %s)", (100, 'Patrick'))
print "=========="
cur.execute('SELECT * FROM foo;')
foo = cur.fetchone()
print foo
bar = cur.fetchone()
print bar

conn.commit()

cur.close()

conn.close()
