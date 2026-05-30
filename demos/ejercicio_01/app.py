##mostrar paginas, conectarse con bases de datos
import web
##permite saber la direccion de la pagina
urls = (
    '/', 'Index',
    '/Clientes', 'Clientes',
    '/Usuario','Usuario',
)
##hace que todoo funcione 
app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        return str(render.index())
   

class Clientes:
    def GET(self):
        return str(render.clientes())
class Usuario:
    def GET(self):
        return str(render.usuario())   
    
##ejecuta el servidor 
if __name__ == "__main__":
    app.run()