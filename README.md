# 🧹 Limpador de Caracteres Invisíveis (Unicode)

Ferramenta feita com [Streamlit](https://streamlit.io) para **limpar textos contaminados por caracteres Unicode invisíveis**.

---

## ✅ Funcionalidades

- Remove e substitui todos os caracteres invisíveis da lista padrão Unicode
- Substitui:
  - Espaços invisíveis → `" "` (espaço comum)
  - Quebras invisíveis → `\n`
- Remove completamente os demais invisíveis (como ZWJ, BOM, etc)
- Valida se o texto final está 100% limpo
- Visualiza o texto com destaques dos problemas

---

## 🚀 Como usar localmente

```bash
git clone https://github.com/seu-usuario/limpador-unicode.git
cd limpador-unicode
pip install -r requirements.txt
streamlit run limpador_unicode_final_validado.py
```

---

## ☁️ Deploy com Streamlit Cloud

1. Crie um repositório no GitHub
2. Suba os arquivos:
   - `limpador_unicode_final_validado.py`
   - `requirements.txt`
3. Acesse https://streamlit.io/cloud
4. Conecte seu repositório e publique seu app

---

## 🧠 Desenvolvido por

**Synap Digital** – A inteligência por trás do seu conteúdo.
