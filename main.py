from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get('/')
def homepage():
    return '<h1></h1>'

serve()