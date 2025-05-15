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
for code in range(0xFE00, 0xFE10):
    if code not in invisible_chars:
        invisible_chars[code] = f"Variation Selector (U+{code:04X})"

# Separar por tipo de substituição
space_like = {chr(code) for code in invisible_chars if code in [0x0020, 0x00A0, 0x2000, 0x2001, 0x2002, 0x2003,
    0x2004, 0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200A, 0x202F, 0x205F, 0x3000]}
newline_like = {'\u000A', '\u000D', chr(0x2028), chr(0x2029)}
invisible_set = set(chr(code) for code in invisible_chars)

def limpar_unicode(texto):
    resultado = ""
    removidos = []
    for c in texto:
        if c in space_like:
            resultado += " "
            removidos.append(ord(c))
        elif c in newline_like or c == "\n":
            resultado += "\n"
            removidos.append(ord(c))
        elif c in invisible_set:
            removidos.append(ord(c))
        else:
            resultado += c
    return resultado, removidos

def validar_ascii(texto):
    return all(32 <= ord(c) <= 126 or c == "\n" for c in texto)

def detectar_outros(texto):
    return [f"U+{ord(c):04X}" for c in texto if ord(c) < 32 or ord(c) > 126 and c != "\n"]

st.set_page_config(page_title="Limpador de Caracteres Invisíveis", layout="centered")
st.title("🧹 Limpador de Caracteres Invisíveis (Unicode)")

texto = st.text_area("Cole seu texto aqui:", height=300)

if st.button("Limpar texto"):
    texto_limpo, removidos = limpar_unicode(texto)

    st.success(f"{len(removidos)} caractere(s) invisível(is) foram removidos ou substituídos.")

    st.markdown("### ✨ Texto limpo (com espaços e quebras normalizados)")
    st.code(texto_limpo, language="markdown")

    if removidos:
        st.markdown("### 📊 Códigos processados")
        contagem = Counter(removidos)
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
st.caption("Ferramenta Synap Digital para auditoria e limpeza rigorosa de caracteres invisíveis.")
