
import os
import random
from datetime import datetime
from fpdf import FPDF

topicos = [
    "Importância do bem-estar animal na sociedade moderna.",
    "Como práticas de autocuidado impactam a saúde mental.",
    "Terapias alternativas para melhorar o bem-estar humano.",
    "Conexão entre humanos e animais: impacto emocional.",
    "Práticas sustentáveis que promovem o bem-estar coletivo."
]

def gerar_artigo():
    titulo = random.choice(topicos)
    slug = titulo.lower().replace(" ", "-").replace(".", "")
    data = datetime.now().strftime('%Y-%m-%d')
    texto_md = f"# {titulo}\n\n*Publicado em {data}*\n\nEste artigo aborda tópicos relacionados ao bem-estar humano e animal.\n"
    os.makedirs("artigos", exist_ok=True)
    path_artigo = f"artigos/{slug}.md"
    with open(path_artigo, "w", encoding="utf-8") as f:
        f.write(texto_md)
    return slug, titulo, texto_md

def gerar_ebook(titulo, slug, conteudo_md):
    os.makedirs("ebooks", exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, conteudo_md)
    path_pdf = f"ebooks/{slug}.pdf"
    pdf.output(path_pdf)

def gerar_pagina_compra(slug, titulo):
    os.makedirs("links", exist_ok=True)
    link = f"https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=SEU_ID_DO_PRODUTO_AQUI"
    html = f"""<html>
<head><title>Comprar: {titulo}</title></head>
<body>
<h1>{titulo}</h1>
<a href="{link}" target="_blank">Comprar Agora</a>
</body>
</html>"""
    path_html = f"links/comprar-{slug}.html"
    with open(path_html, "w", encoding="utf-8") as f:
        f.write(html)

def publicar_git():
    os.system("git config --global user.email 'bot@github.com'")
    os.system("git config --global user.name 'GitHub Bot'")
    os.system("git add .")
    os.system("git commit -m 'Conteúdo gerado automaticamente' || echo 'Nada novo'")
    os.system("git push origin main")

slug, titulo, conteudo_md = gerar_artigo()
gerar_ebook(titulo, slug, conteudo_md)
gerar_pagina_compra(slug, titulo)
publicar_git()
