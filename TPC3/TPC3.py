import re

def markdown_to_html(md_text):
    # Cabeçalhos
    md_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md_text, flags=re.MULTILINE)

    # Bold (negrito)
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md_text)

    # Itálico
    md_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md_text)

    # Links
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', md_text)

    # Imagem
    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', md_text)

    # Listas numeradas
    def parse_ordered_list(match):
        items = match.group(0).strip().split('\n')
        html_list = "<ol>\n"
        for item in items:
            item_text = re.sub(r'^\d+\.\s+', '', item)
            html_list += f"<li>{item_text}</li>\n"
        html_list += "</ol>"
        return html_list

    md_text = re.sub(r'(\d+\..+(\n\d+\..+)*)', parse_ordered_list, md_text)

    return md_text


if __name__ == "__main__":
    # Lê um arquivo markdown (exemplo.md) e converte para HTML
    with open('exemplo.md', 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    html = markdown_to_html(markdown_text)

    # Salva em um arquivo HTML
    with open('exemplo.html', 'w', encoding='utf-8') as file:
        file.write(html)

    print("Conversão concluída! Arquivo 'exemplo.html' gerado.")
