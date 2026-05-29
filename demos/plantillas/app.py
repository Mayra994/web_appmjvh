##mostrar paginas, conectarse con bases de datos
import web
##permite saber la direccion de la pagina
urls = (
    '/', 'Index'
)
##hace que todoo funcione 
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
##ejecuta el servidor 
if __name__ == "__main__":
    app.run()