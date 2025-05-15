import streamlit as st

# Lista completa dos caracteres invisíveis
unicode_invisiveis = [
    0x0020, 0x00A0, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004,
    0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200A, 0x202F,
    0x205F, 0x3000, 0x200B, 0x200C, 0x200D, 0x2060, 0x200E,
    0x200F, 0x202A, 0x202B, 0x202C, 0x202D, 0x202E, 0x00AD,
    0x034F, 0x061C, 0xFE0E, 0xFE0F, 0xFEFF, 0xFFF9, 0xFFFA,
    0xFFFB
] + list(range(0xFE00, 0xFE10))  # FE00–FE0F

# Separar por função
espacos_invisiveis = {
    0x0020, 0x00A0, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004,
    0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200A,
    0x202F, 0x205F, 0x3000
}
quebras_invisiveis = {0x000A, 0x2028, 0x2029}
demais_remover = set(unicode_invisiveis) - espacos_invisiveis - quebras_invisiveis

espacos_set = set(chr(c) for c in espacos_invisiveis)
quebras_set = set(chr(c) for c in quebras_invisiveis)
remover_set = set(chr(c) for c in demais_remover)

def limpar(texto):
    texto_limpo = ""
    removidos = []
    for c in texto:
        code = ord(c)
        if c in espacos_set:
            texto_limpo += " "
            removidos.append(f"U+{code:04X}")
        elif c in quebras_set:
            texto_limpo += "\n"
            removidos.append(f"U+{code:04X}")
        elif c in remover_set:
            removidos.append(f"U+{code:04X}")
        else:
            texto_limpo += c
    return texto_limpo, removidos

# Interface
st.set_page_config(page_title="Limpador de Caracteres Invisíveis", layout="centered")
st.title("🧹 Limpador de Caracteres Invisíveis (Unicode)")
texto = st.text_area("Cole seu texto aqui:", height=300)

if st.button("Limpar texto"):
    texto_limpo, removidos = limpar(texto)

    st.success(f"{len(removidos)} caractere(s) invisível(is) foram removidos ou convertidos.")

    st.markdown("### ✨ Texto limpo (com espaços e parágrafos preservados)")
    st.code(texto_limpo, language="markdown")

    if removidos:
        from collections import Counter
        contagem = Counter(removidos)
        st.markdown("### 📊 Códigos removidos ou convertidos")
        for cod, n in contagem.items():
            st.markdown(f"- `{cod}`: {n}×")

    st.markdown("### 🔍 Visualização com destaques")
    destaque = ""
    for c in texto:
        code = ord(c)
        if c in remover_set or c in espacos_set or c in quebras_set:
            destaque += f'<span style="background-color:#FFCDD2;padding:2px;margin:1px;border-radius:4px;">U+{code:04X}</span>'
        else:
            safe = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            destaque += safe
    st.markdown(
        f"<div style='font-family:monospace;background:#F9F9F9;border-radius:8px;padding:10px;'>{destaque}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption("Ferramenta Synap Digital para limpeza precisa de caracteres invisíveis sem comprometer espaçamentos ou parágrafos.")
