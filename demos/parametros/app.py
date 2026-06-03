import web

urls = (
    '/', 'Index',
    '/, parametros','Parametros'

)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
    
class Parametros:
    def GET(self):
        titulo = "Título desde python"
        descripcion = """Lorem ipsum dolor sit amet consectetur adipiscing elit duis nulla, metus sem imperdiet varius natoque ultricies congue sapien tincidunt scelerisque, suscipit in mollis sociosqu feugiat sed massa hendrerit. Quisque in eu sociis fusce parturient pellentesque maecenas, curae sapien urna conubia odio tempus nisi vehicula, posuere ornare potenti consequat congue condimentum. Eleifend sem nisi nullam faucibus est ac lobortis, cum laoreet aptent penatibus nunc aliquet quisque, montes aliquam gravida egestas tristique et.

Suscipit velit egestas auctor penatibus hac tincidunt ornare, ridiculus praesent phasellus odio accumsan sociis, mauris arcu quis ultricies elementum rhoncus. Nam nec duis id purus dis penatibus habitasse viverra ornare, dui urna magna phasellus vehicula suscipit vestibulum litora suspendisse enim, in interdum velit sagittis integer mattis habitant quisque. Convallis nascetur facilisis condimentum consequat quam egestas sem parturient litora, phasellus lacus suscipit scelerisque ligula viverra nunc neque cubilia quis, dictumst pulvinar montes mus praesent posuere blandit maecenas."""

        return render.parametros(titulo,descripcion)    
if __name__ == "__main__":
    app.run()