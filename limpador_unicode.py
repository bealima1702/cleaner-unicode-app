import streamlit as st
import unicodedata
from collections import Counter

# Lista completa dos caracteres invisíveis fornecidos
unicode_invisiveis = {
    0x0020, 0x00A0, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005,
    0x2006, 0x2007, 0x2008, 0x2009, 0x200A, 0x202F, 0x205F, 0x3000,
    0x200B, 0x200C, 0x200D, 0x2060, 0x200E, 0x200F, 0x202A, 0x202B,
    0x202C, 0x202D, 0x202E, 0x00AD, 0x034F, 0x061C,
    0xFE0E, 0xFE0F, 0xFEFF, 0xFFF9, 0xFFFA, 0xFFFB
} | set(range(0xFE00, 0xFE10))

espacos_invisiveis = {
    0x0020, 0x00A0, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005,
    0x2006, 0x2007, 0x2008, 0x2009, 0x200A, 0x202F, 0x205F, 0x3000
}

unicode_set = set(chr(code) for code in unicode_invisiveis)
espacos_set = set(chr(code) for code in espacos_invisiveis)

def limpar_texto(texto):
    texto = unicodedata.normalize("NFKC", texto)
    texto = texto.replace(chr(0x00AD), "")  # redundante para garantir remoção do Soft Hyphen
    texto_limpo = ""
    removidos = []

    for c in texto:
        if c in espacos_set:
            texto_limpo += " "
            removidos.append(ord(c))
        elif c in unicode_set:
            removidos.append(ord(c))
        else:
            texto_limpo += c

    return texto_limpo, removidos

def detectar_residuos(texto):
    return [f"U+{ord(c):04X}" for c in texto if ord(c) in unicode_invisiveis]

st.set_page_config(page_title="Limpador Preciso de Invisíveis", layout="centered")
st.title("🧹 Limpador de Caracteres Invisíveis (Unicode)")

texto = st.text_area("Cole seu texto aqui:", height=300)

if st.button("Limpar texto"):
    texto_limpo, removidos = limpar_texto(texto)
    st.success(f"{len(removidos)} caractere(s) invisível(is) foram removidos ou substituídos.")

    st.markdown("### ✨ Texto limpo")
    st.code(texto_limpo, language="markdown")

    if removidos:
        contagem = Counter(removidos)
        st.markdown("### 📊 Códigos removidos/substituídos")
        for cod, count in contagem.items():
            st.markdown(f"- `U+{cod:04X}`: {count}×")

    residuos = detectar_residuos(texto_limpo)
    if residuos:
        st.error("⚠️ Ainda restam invisíveis no texto final:")
        for cod, n in Counter(residuos).items():
            st.markdown(f"- `{cod}`: {n}x")
    else:
        st.info("✅ O texto final está 100% limpo de invisíveis.")

    st.markdown("### 🔍 Destaques no original")
    destaque = ""
    for c in texto:
        code = ord(c)
        if code in unicode_invisiveis:
            destaque += f'<span style="background-color:#FFCDD2;padding:2px;margin:1px;border-radius:4px;">U+{code:04X}</span>'
        else:
            safe = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            destaque += safe
    st.markdown(
        f"<div style='font-family:monospace;background:#F9F9F9;border-radius:8px;padding:10px;'>{destaque}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("Ferramenta Synap Digital para limpeza de caracteres invisíveis com substituição inteligente.")
