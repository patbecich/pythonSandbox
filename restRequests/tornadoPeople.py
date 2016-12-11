
myDict = {}

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1,'')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


import tornado.ioloop
import tornado.web

import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class LookupHandler(tornado.web.RequestHandler):
    def post(self):
        data = self.request.body
        print "request payload: "+str(data)
        requestDict = json.loads(data)
        print "request payload dict: "+str(requestDict)

        requestLabel = requestDict['label']
        requestName = requestDict['name']

        person = lookup(global myDict, requestLabel, requestName)

        self.write(person)
        

# class AgeHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("age: "+str(age))
#     def post(self):
#         data = self.request.body
#         age = data
#         print "age: "+str(age)
#         self.write("age: "+str(age))


        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/lookup", LookupHandler),
        # (r"/goodbye", GoodbyeHandler),
        # (r"/age", AgeHandler)
    ])

if __name__ == "__main__":
    init(global myDict)
    store(myDict,'Patrick James Becich')
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

