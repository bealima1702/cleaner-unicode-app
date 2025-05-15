import streamlit as st
from collections import Counter

# Lista completa dos caracteres invisíveis a serem removidos
invisible_chars = {
    0x0020, 0x00A0, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005,
    0x2006, 0x2007, 0x2008, 0x2009, 0x200A, 0x202F, 0x205F, 0x3000,
    0x200B, 0x200C, 0x200D, 0x2060, 0x200E, 0x200F, 0x202A, 0x202B,
    0x202C, 0x202D, 0x202E, 0x00AD, 0x034F, 0x061C,
    0xFE0E, 0xFE0F, 0xFEFF, 0xFFF9, 0xFFFA, 0xFFFB
} | set(range(0xFE00, 0xFE10))

invisible_set = set(chr(code) for code in invisible_chars)

def limpar_unicode_total(texto):
    texto_limpo = ""
    removidos = []
    for c in texto:
        if c in invisible_set:
            removidos.append(ord(c))
        else:
            texto_limpo += c
    return texto_limpo, removidos

def validar_ascii(texto):
    return all(32 <= ord(c) <= 126 or c == "\n" for c in texto)

def detectar_outros(texto):
    return [f"U+{ord(c):04X}" for c in texto if ord(c) < 32 or ord(c) > 126 and c != "\n"]

st.set_page_config(page_title="Limpador Total de Invisíveis", layout="centered")
st.title("🧹 Limpador de Caracteres Invisíveis (Unicode)")

texto = st.text_area("Cole seu texto aqui:", height=300)

if st.button("Limpar texto"):
    texto_limpo, removidos = limpar_unicode_total(texto)

    st.success(f"{len(removidos)} caractere(s) invisível(is) foram removidos.")

    st.markdown("### ✨ Texto limpo (sem nenhum invisível da lista)")
    st.code(texto_limpo, language="markdown")

    if removidos:
        contagem = Counter(removidos)
        st.markdown("### 📊 Códigos removidos")
        for cod, count in contagem.items():
            st.markdown(f"- `U+{cod:04X}`: {count}×")

    if not validar_ascii(texto_limpo):
        suspeitos = detectar_outros(texto_limpo)
        st.warning("⚠️ Ainda restam caracteres fora da faixa ASCII:")
        for s in Counter(suspeitos).items():
            st.markdown(f"- `{s[0]}`: {s[1]}x")
    else:
        st.info("✅ O texto final contém apenas ASCII padrão + \n.")

    st.markdown("### 🔍 Destaques no original")
    destaque = ""
    for c in texto:
        code = ord(c)
        if c in invisible_set:
            destaque += f'<span style="background-color:#FFCDD2;padding:2px;margin:1px;border-radius:4px;">U+{code:04X}</span>'
        else:
            safe = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            destaque += safe
    st.markdown(
        f"<div style='font-family:monospace;background:#F9F9F9;border-radius:8px;padding:10px;'>{destaque}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("Ferramenta Synap Digital para remoção total de caracteres invisíveis Unicode.")
