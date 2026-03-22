from fasthtml.common import fast_app, serve, Titled
from componentes import gerar_titulo
from componentes import gerar_formulario

app, routes = fast_app()

@routes('/')
def homepage():
    formulario = gerar_formulario()
    return formulario

serve()