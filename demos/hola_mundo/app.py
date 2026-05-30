##mostrar paginas, conectarse con bases de datos
import web
##permite saber la direccion de la pagina
urls = (
    '/', 'Index'
)
##hace que todoo funcione 
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola mundo desde web.py'
##ejecuta el servidor 
if __name__ == "__main__":
    app.run()