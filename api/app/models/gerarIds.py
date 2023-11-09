import random
import string

def gerar_id_8_caracteres():
    caracteres = string.ascii_letters + string.digits  # letras maiúsculas, minúsculas e dígitos
    id_gerado = ''.join(random.choice(caracteres) for _ in range(8))
    return id_gerado