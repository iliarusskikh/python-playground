import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "<h1> Hello </h1>"

cherrypy.tree.mount(Root(), "/", config={'/':{'tools.staticdir.on': True, 'tools.staticdir.dir': './'}})
cherrypy.engine.start()
cherrypy.engine.block()

