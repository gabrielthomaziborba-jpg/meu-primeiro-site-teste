from fasthtml.common import Div, H1, P, Form, Button, Input

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P('Esse site foi criado em fastHTML')
    )
def gerar_formulario():
    formulario = Form(
        Input(type='text', name='tarefa', placeholder='Insira algo só pra eu testar'),
        Button('Enviar'),
        method='post',
        action='/'
    )
    return formulario

def lista_tarefas():
    pass
