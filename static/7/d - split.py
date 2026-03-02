import json
import os

pasta = os.path.dirname(os.path.abspath(__file__))

pagina_file = os.path.join(pasta, "a - pagina.txt")
with open(pagina_file, "r", encoding="utf-8") as f:
    pagina = f.readline().strip()

#pagina="2"

INPUT_JSON = os.path.join(pasta, pagina + "traducao.json")
OUTPUT_JSON = os.path.join(pasta, pagina + "split.json")

# Ler JSON
with open(INPUT_JSON, "r", encoding="utf-8") as f:
    dados = json.load(f)

# Função para aplicar split em strings
def split_strings(obj):
    novo_obj = {}
    for chave, valor in obj.items():
        if isinstance(valor, str):
            # aplica split como no JS
            novo_obj[chave] = valor.split(" ")
        else:
            novo_obj[chave] = valor
    return novo_obj

# Aplicar split em cada item
dados_split = [split_strings(item) for item in dados]

# Salvar novo JSON
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(dados_split, f, indent=4, ensure_ascii=False)

print(f"Arquivo com strings divididas salvo em '{OUTPUT_JSON}'.")