
# vim: syntax=python
import sys
# Na linha abaixo basta  informar o caminho completo para o arquivo bin/activate_this.py dentro da pasta do virtual env
activate_this = '/home/artigo/flask-na-kinghost/apps_wsgi/testflask/virtual_env/bin/activate_this.py'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
sys.path.append('/home/artigo/flask-na-kinghost/apps_wsgi/testflask')
from run import app as application