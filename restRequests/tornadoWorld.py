
import tornado.ioloop
import tornado.web

import psycopg2

print psycopg2

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="YellowDog",
    host="127.0.0.1",
    port="5433")
print conn
cur = conn.cursor()
cur.execute('SELECT * FROM country;')

global cur2
cur2 = conn.cursor()

class Query(tornado.web.RequestHandler):
    def post(self):
        queryString = self.request.body
        print queryString
        cur2.execute(queryString)
        self.write('Number of rows: '+ str(cur2.rowcount))

    def get(self):
        row = cur2.fetchone()
        self.write(str(row))

class Countries(tornado.web.RequestHandler):
    def get(self):
        foo = cur.fetchone()

       # conn.commit()
       # cur.close()
       # conn.close()

       # print 'Cursor and connection closed'

        self.write(str(foo))


class TenRows(tornado.web.RequestHandler):
    def get(self):
        for i in range(9):
            bar = cur.fetchone()
            self.write(str(bar))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/countries", Countries),
        (r"/tenrows", TenRows),
        (r"/query", Query),
        # (r"/goodbye", GoodbyeHandler),
        # (r"/age", AgeHandler)
    ])
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
