import web

urls = (
    '/', 'Index',
    '/contactos', 'Contactos'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.index()
   

class Contactos:
    def GET(self):
        return render.contactos()


if __name__ == "__main__":
    app.run() 