from jinja2 import FileSystemLoader,Environment

#variavel loader que vai carregar o templete do html (no caso da pastas de template) 
loader = FileSystemLoader('templates')

#criação do ambiente que recebe a classe enviromment que utiliza o filesystemloader ( loader ) 
env = Environment(loader=loader)

#variavel template que recebe o ambiente(env) é o get_template()[uma função] {que recebe o template html}
template = env.get_template('homepage.html')

#diferente da versão simple.py que usamos um print usaremos o open para gerar um html na pasta output
file = open('output/index.html', 'w')

#temos o template temos que renderizar que nem fizemos no exemplo simple.py (dentro de uma variavel)
render = template.render(titulo="teste com jinja2", cor_fundo= "#000", cor_do_texto="#FFF",nome="testandojinja")

# o write escreve dento do arquivo nossa renderização(render)
file.write(render)

#fechar o file
file.close()
