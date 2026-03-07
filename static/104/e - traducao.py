import json
from deep_translator import GoogleTranslator
import os


pasta = os.path.dirname(os.path.abspath(__file__))

pagina_file = os.path.join(pasta, "c - pagina.txt")
with open(pagina_file, "r", encoding="utf-8") as f:
    pagina = f.readline().strip()
# pagina="2"

INPUT_JSON = os.path.join(pasta, pagina + "mouse.json")
OUTPUT_JSON = os.path.join(pasta, pagina + "traducao.json")

# Função de tradução
def traduzir(texto):
    try:
        return GoogleTranslator(source='en', target='pt').translate(texto)
    except Exception as e:
        print(f"Erro ao traduzir '{texto}': {e}")
        return ""

# Ler JSON
with open(INPUT_JSON, "r", encoding="utf-8") as f:
    dados = json.load(f)

# Traduzir cada item
for item in dados:
    texto_en = item.get("en", "").strip()
    if texto_en:
        # Tradução literal
        item["ptbr"] = traduzir(texto_en)
        # ptbrpp = mesma tradução por enquanto
        item["ptbrpp"] = traduzir(texto_en)

# Salvar JSON traduzido
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print(f"Tradução concluída. Arquivo salvo como '{OUTPUT_JSON}'.")