# vim: syntax=python
import sys
# Na linha abaixo basta  informar o caminho completo para o arquivo bin/activate_this.py dentro da pasta do virtual env
activate_this = '/home/pbeedifica/www/questionario_hablab/__pycache__/run.cpython-312.pyc'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=run.cpython-312.pyc))
sys.path.append('/home/pbeedifica/www/questionario_hablab/__pycache__/')
from run import app as application