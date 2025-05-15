import streamlit as st

# Lista completa de caracteres invisíveis/suspeitos fornecidos
invisible_unicode = [
    0x00A0, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005,
    0x2006, 0x2007, 0x2008, 0x2009, 0x200A, 0x202F, 0x205F,
    0x3000, 0x200B, 0x200C, 0x200D, 0x2060, 0x200E, 0x200F,
    0x202A, 0x202B, 0x202C, 0x202D, 0x202E, 0x00AD, 0x034F,
    0x061C, 0xFE0E, 0xFE0F, 0xFEFF, 0xFFF9, 0xFFFA, 0xFFFB
] + list(range(0xFE00, 0xFE10))

invisible_set = set(chr(c) for c in invisible_unicode)

def is_safe_ascii(c):
    return 32 <= ord(c) <= 126  # ASCII imprimível: espaço até ~

st.set_page_config(page_title="Limpador Seguro ASCII", layout="centered")
st.title("🛡️ Limpador Total de Caracteres Invisíveis e Não ASCII")

texto = st.text_area("Cole seu texto aqui:", height=300)

if st.button("Limpar texto"):
    removidos = []
    texto_limpo = ""
    for c in texto:
        if c in invisible_set:
            removidos.append(ord(c))
        elif not is_safe_ascii(c):
            removidos.append(ord(c))
        else:
            texto_limpo += c

    if removidos:
        st.success(f"{len(removidos)} caractere(s) invisível(is) ou fora da faixa ASCII foram removidos.")
        st.markdown("### ✨ Texto limpo (somente ASCII imprimível)")
        st.code(texto_limpo, language="markdown")

        # Visualização com destaques
        st.markdown("### 🔍 Visualização com removidos destacados")
        destaque = ""
        for c in texto:
            if c in invisible_set or not is_safe_ascii(c):
                destaque += f'<span style="background-color:#FFCDD2;padding:2px;margin:1px;border-radius:4px;">U+{ord(c):04X}</span>'
            else:
                safe = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                destaque += safe
        st.markdown(
            f"<div style='font-family:monospace;background:#F9F9F9;border-radius:8px;padding:10px;'>{destaque}</div>",
            unsafe_allow_html=True
        )
    else:
        st.info("Nenhum caractere problemático foi encontrado.")

st.markdown("---")
st.caption("Ferramenta Synap Digital para limpeza rigorosa de textos com segurança ASCII.")
