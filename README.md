# 🧹 Limpador de Caracteres Invisíveis (Unicode)

Esta é uma ferramenta desenvolvida com [Streamlit](https://streamlit.io) para identificar e remover caracteres invisíveis Unicode de textos — como `Zero Width Space`, `Non-breaking Space`, `Soft Hyphen`, entre outros.

---

## 🚀 Como usar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/limpador-unicode.git
cd limpador-unicode
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute localmente:
```bash
streamlit run limpador_unicode.py
```

---

## 🌐 Deploy Online (recomendado)

Você pode publicar facilmente via [Streamlit Cloud](https://streamlit.io/cloud).  
Basta subir esse repositório no GitHub e conectar no painel da Streamlit.

---

## ✨ Funcionalidades

- Limpa caracteres invisíveis automaticamente
- Informa quantos e quais foram removidos
- Mostra o texto limpo pronto para cópia
- Visualiza com destaque onde os invisíveis estavam
- Interface simples, acessível e responsiva

---

## 📘 Lista de caracteres removidos

Inclui, entre outros:
- `U+200B` Zero Width Space
- `U+00A0` Non-breaking Space
- `U+00AD` Soft Hyphen
- `U+FEFF` BOM
- Todos os Variation Selectors (`U+FE00–U+FE0F`)

---

## 🧠 Desenvolvido por

**Synap Digital** – Inteligência por trás do seu conteúdo.
