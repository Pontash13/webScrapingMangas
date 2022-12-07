import random
import string
from pathlib import Path


#gera um palavra aleatoria como dsfafdjafj
def gera_nome_aleatorio():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(25))
