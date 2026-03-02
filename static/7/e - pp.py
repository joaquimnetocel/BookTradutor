import json
import os
from deep_translator import GoogleTranslator

# ==============================
# Caminhos
# ==============================
pasta = os.path.dirname(os.path.abspath(__file__))
pagina_file = os.path.join(pasta, "a - pagina.txt")
with open(pagina_file, "r", encoding="utf-8") as f:
    pagina = f.readline().strip()

arquivo_entrada = os.path.join(pasta, pagina + "split.json")  # seu arquivo original
arquivo_saida = os.path.join(pasta, pagina + ".json")  # novo arquivo

# ==============================
# Tradutor EN → PT-BR
# ==============================
translator = GoogleTranslator(source="en", target="pt")

# ==============================
# Função: traduz palavra por palavra
# ==============================
def traduzir_lista(lista_en):
    resultado = []

    for palavra in lista_en:
        try:
            traducao = translator.translate(palavra)
            resultado.append(traducao.upper())
        except Exception as e:
            print(f"Erro ao traduzir '{palavra}': {e}")
            resultado.append(palavra)

    return resultado


# ==============================
# Ler JSON original
# ==============================
with open(arquivo_entrada, "r", encoding="utf-8") as f:
    dados = json.load(f)

# ==============================
# Traduzir cada item
# ==============================
for item in dados:
    if isinstance(item.get("en"), list):
        item["ptbrpp"] = traduzir_lista(item["en"])

# ==============================
# Salvar em novo arquivo
# ==============================
with open(arquivo_saida, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print("✅ Tradução concluída.")
print("📄 Arquivo salvo em:", arquivo_saida)