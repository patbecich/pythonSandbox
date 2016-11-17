import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


        

class GoodbyeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Goodbye!")


age = "nothing yet"

class AgeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("age: "+str(age))
    def post(self):
        data = self.request.body
        age = data
        print "age: "+str(age)
        self.write("age: "+str(age))


        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/goodbye", GoodbyeHandler),

        (r"/age", AgeHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
