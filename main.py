from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get('/')
def homepage():
    return '<h1>Site do Gabriel!!!</h1>'

serve()