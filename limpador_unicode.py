import streamlit as st
from collections import Counter

# Dicionário expandido com todos os caracteres invisíveis Unicode fornecidos
invisible_chars = {
    0x0020: "Space (U+0020)",
    0x00A0: "Non-breaking Space (U+00A0)",
    0x2000: "En Quad (U+2000)",
    0x2001: "Em Quad (U+2001)",
    0x2002: "En Space (U+2002)",
    0x2003: "Em Space (U+2003)",
    0x2004: "Three-Per-Em Space (U+2004)",
    0x2005: "Four-Per-Em Space (U+2005)",
    0x2006: "Six-Per-Em Space (U+2006)",
    0x2007: "Figure Space (U+2007)",
    0x2008: "Punctuation Space (U+2008)",
    0x2009: "Thin Space (U+2009)",
    0x200A: "Hair Space (U+200A)",
    0x202F: "Narrow No-Break Space (U+202F)",
    0x205F: "Medium Mathematical Space (U+205F)",
    0x3000: "Ideographic Space (U+3000)",
    0x200B: "Zero Width Space (U+200B)",
    0x200C: "Zero Width Non-Joiner (U+200C)",
    0x200D: "Zero Width Joiner (U+200D)",
    0x2060: "Word Joiner (U+2060)",
    0x200E: "Left-to-Right Mark (U+200E)",
    0x200F: "Right-to-Left Mark (U+200F)",
    0x202A: "Left-to-Right Embedding (U+202A)",
    0x202B: "Right-to-Left Embedding (U+202B)",
    0x202C: "Pop Directional Formatting (U+202C)",
    0x202D: "Left-to-Right Override (U+202D)",
    0x202E: "Right-to-Left Override (U+202E)",
    0x00AD: "Soft Hyphen (U+00AD)",
    0x034F: "Combining Grapheme Joiner (U+034F)",
    0x061C: "Arabic Letter Mark (U+061C)",
    0xFE0E: "Variation Selector-15 (U+FE0E)",
    0xFE0F: "Variation Selector-16 (U+FE0F)",
    0xFEFF: "Byte Order Mark (U+FEFF)",
    0xFFF9: "Interlinear Annotation Anchor (U+FFF9)",
    0xFFFA: "Interlinear Annotation Separator (U+FFFA)",
    0xFFFB: "Interlinear Annotation Terminator (U+FFFB)"
}

# Adiciona o intervalo de FE00 a FE0F, caso ainda não esteja incluso
for code in range(0xFE00, 0xFE10):
    if code not in invisible_chars:
        invisible_chars[code] = f"Variation Selector (U+{code:04X})"

unicode_set = set(invisible_chars.keys())

st.title("🧹 Limpador de Caracteres Invisíveis (Unicode)")

texto = st.text_area("Cole seu texto aqui:", height=250)

if st.button("Limpar texto"):
    texto_limpo = ""
    removidos = []

    for c in texto:
        code = ord(c)
        if code in unicode_set:
            removidos.append(code)
            if code == 0x0020:
                texto_limpo += " "  # substitui explicitamente U+0020
        else:
            texto_limpo += c

    st.success(f"{len(removidos)} caractere(s) invisível(is) foram removidos ou substituídos.")

    if removidos:
        contagem = Counter(removidos)
        st.markdown("### 📊 Códigos removidos/substituídos")
        for code, count in contagem.items():
            label = f"U+{code:04X}"
            nome = invisible_chars[code]
            st.markdown(f"**{count}×** <span style='background-color:#FFCDD2;padding:2px 6px;border-radius:4px;color:black;'> {label} {nome.split('(')[0].strip()} </span>", unsafe_allow_html=True)

    st.markdown("### ✨ Texto limpo")
    st.code(texto_limpo, language="markdown")

    st.markdown("### 🔍 Destaques removidos no original")
    destaque = ""
    for c in texto:
        code = ord(c)
        if code in unicode_set:
            destaque += f'<span style="background-color:#FFCDD2;padding:2px;margin:1px;border-radius:4px;">U+{code:04X}</span>'
        else:
            safe = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            destaque += safe
    st.markdown(
        f"<div style='font-family:monospace;background:#F9F9F9;border-radius:8px;padding:10px;'>{destaque}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("Limpador Synap Digital – com remoção precisa e sem corromper acentuação.")
