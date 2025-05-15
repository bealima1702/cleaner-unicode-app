import streamlit as st

# Lista de caracteres invisíveis a substituir por espaço
espacos_unicode = {
    0x0020, 0x00A0, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004,
    0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200A, 0x202F,
    0x205F, 0x3000
}

# Lista de caracteres invisíveis a remover totalmente
invisiveis_a_remover = {
    0x200B, 0x200C, 0x200D, 0x2060, 0x200E, 0x200F, 0x202A, 0x202B,
    0x202C, 0x202D, 0x202E, 0x00AD, 0x034F, 0x061C, 0xFE0E, 0xFE0F,
    0xFEFF, 0xFFF9, 0xFFFA, 0xFFFB
} | set(range(0xFE00, 0xFE10))

# Quebras invisíveis que devem virar \n
quebras_unicode = {
    0x000A,  # LF
    0x000D,  # CR
    0x2028,  # Line Separator
    0x2029   # Paragraph Separator
}

# Conjuntos de decisão
substituir_por_espaco = set(chr(c) for c in espacos_unicode)
remover = set(chr(c) for c in invisiveis_a_remover)
substituir_por_queebra = set(chr(c) for c in quebras_unicode)

def limpar_texto(texto):
    resultado = ""
    removidos = []
    for c in texto:
        if c in substituir_por_espaco:
            resultado += " "
        elif c in substituir_por_queebra:
            resultado += "\n"
        elif c in remover:
            removidos.append(f"U+{ord(c):04X}")
        else:
            resultado += c
    return resultado, removidos

st.set_page_config(page_title="Limpador Final Unicode", layout="centered")
st.title("🧼 Limpador Final de Caracteres Unicode (Espaço e Parágrafo)")

texto = st.text_area("Cole seu texto aqui:", height=300)

if st.button("Limpar texto"):
    texto_limpo, removidos = limpar_texto(texto)

    st.success(f"{len(removidos)} caractere(s) invisível(is) foram removidos ou convertidos.")

    st.markdown("### ✨ Texto limpo (com espaços e quebras normalizadas)")
    st.code(texto_limpo, language="markdown")

    if removidos:
        st.markdown("### 🔍 Códigos removidos")
        contagem = {}
        for cod in removidos:
            contagem[cod] = contagem.get(cod, 0) + 1
        for cod, n in contagem.items():
            st.markdown(f"- `{cod}`: {n}x")

    st.markdown("### 🔎 Visualização com destaques")
    destaque = ""
    for c in texto:
        code = ord(c)
        if c in remover or c in substituir_por_espaco or c in substituir_por_queebra:
            destaque += f'<span style="background-color:#FFCDD2;padding:2px;margin:1px;border-radius:4px;">U+{code:04X}</span>'
        else:
            safe = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            destaque += safe
    st.markdown(
        f"<div style='font-family:monospace;background:#F9F9F9;border-radius:8px;padding:10px;'>{destaque}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("Ferramenta Synap Digital para limpeza e normalização rigorosa de espaços e parágrafos.")
