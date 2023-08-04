import jinja2

models = "olá {{ nome }}, bem vindo ao inferno {{ universidade }} Sua assinatura deve ser feita com o email: {{email}}"



dados = [
    ["sqlalchemy alembic","sti", "sqlachemypai@gmail.com"],
    ["alembic sqlalchemt","jairouniversidade","alembicfilhodaputa@gmail"],
    ["jovinho filho do sqlalchemy","ufpe", "jovinhu@cachorro.com"]
]

template = jinja2.Template(models)

for dado in dados:
    print(template.render(nome=dado[0],universidade=dado[1],email=dado[2]))
        