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

class Index:
    def GET(self):
        return 'Hola mundo desde web.py'

class Clientes:
    def GET(self):
        return 'Esta es la pagina de CLIENTES'   
class Usuario:
    def GET(self):
        return 'Esta es la pagina de USUARIOS'         
    
##ejecuta el servidor 
if __name__ == "__main__":
    app.run()