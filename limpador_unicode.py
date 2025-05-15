import streamlit as st

# Dicionário de caracteres invisíveis (Unicode + nomes)
invisible_map = {
    0x0020: "Space",
    0x00A0: "Non-breaking Space",
    0x2000: "En Quad",
    0x2001: "Em Quad",
    0x2002: "En Space",
    0x2003: "Em Space",
    0x2004: "Three-Per-Em Space",
    0x2005: "Four-Per-Em Space",
    0x2006: "Six-Per-Em Space",
    0x2007: "Figure Space",
    0x2008: "Punctuation Space",
    0x2009: "Thin Space",
    0x200A: "Hair Space",
    0x202F: "Narrow No-Break Space",
    0x205F: "Medium Mathematical Space",
    0x3000: "Ideographic Space",
    0x200B: "Zero Width Space",
    0x200C: "Zero Width Non-Joiner",
    0x200D: "Zero Width Joiner",
    0x2060: "Word Joiner",
    0x200E: "Left-to-Right Mark",
    0x200F: "Right-to-Left Mark",
    0x202A: "Left-to-Right Embedding",
    0x202B: "Right-to-Left Embedding",
    0x202C: "Pop Directional Formatting",
    0x202D: "Left-to-Right Override",
    0x202E: "Right-to-Left Override",
    0x00AD: "Soft Hyphen",
    0x034F: "Combining Grapheme Joiner",
    0x061C: "Arabic Letter Mark",
    0xFE0E: "Variation Selector-15",
    0xFE0F: "Variation Selector-16",
    0xFEFF: "Byte Order Mark",
    0xFFF9: "Interlinear Annotation Anchor",
    0xFFFA: "Interlinear Annotation Separator",
    0xFFFB: "Interlinear Annotation Terminator"
}
for code in range(0xFE00, 0xFE10):
    invisible_map.setdefault(code, f"Variation Selector (U+{code:04X})")

invisible_set = set(chr(c) for c in invisible_map)

# Interface
st.set_page_config(page_title="Limpador de Caracteres Invisíveis", layout="centered")
st.title("🧹 Limpador de Caracteres Invisíveis (Unicode)")
texto = st.text_area("Cole seu texto aqui:", height=300)

if st.button("Limpar texto"):
    removidos = [c for c in texto if c in invisible_set]
    texto_limpo = ''.join(c for c in texto if c not in invisible_set)

    if removidos:
        st.success(f"{len(removidos)} caractere(s) invisível(is) foram removidos.")
        st.markdown("### ✨ Texto limpo")
        st.code(texto_limpo, language="markdown")

        # Visualização com destaques
        st.markdown("### 🔍 Visualização com remoções destacadas")
        destaque = ""
        for c in texto:
            if c in invisible_set:
                code = ord(c)
                destaque += f'<span style="background-color:#FFCDD2;padding:2px;border-radius:4px;margin:1px;" title="{invisible_map[code]}">U+{code:04X}</span>'
            else:
                safe = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                destaque += safe
        st.markdown(
            f"<div style='font-family:monospace;line-height:1.6;background:#f9f9f9;border-radius:8px;padding:10px'>{destaque}</div>",
            unsafe_allow_html=True
        )
    else:
        st.info("Nenhum caractere invisível foi encontrado.")

st.markdown("---")
st.caption("Ferramenta Synap Digital para limpeza de texto e remoção de caracteres invisíveis.")
