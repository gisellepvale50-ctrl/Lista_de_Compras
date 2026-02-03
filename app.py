import streamlit as st
import os

# --- Configurações Iniciais ---
st.set_page_config(page_title="Lista de Compras Pro", page_icon="🍎")

# Arquivo onde a lista será salva
ARQUIVO_DADOS = "lista_compras.txt"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            return [linha.strip() for linha in f.readlines()]
    return []

def salvar_dados(lista):
    with open(ARQUIVO_DADOS, "w") as f:
        for item in lista:
            f.write(f"{item}\n")

# Inicializa o estado da lista
if 'lista' not in st.session_state:
    st.session_state.lista = carregar_dados()

# --- Interface ---
st.title("🛒 Minha Lista Interativa")

# Input para novo item
with st.form("add_item", clear_on_submit=True):
    novo_item = st.text_input("Adicione algo à lista:")
    botao_add = st.form_submit_button("Adicionar")

if botao_add and novo_item:
    st.session_state.lista.append(novo_item)
    salvar_dados(st.session_state.lista)
    st.rerun()

st.subheader("Itens Pendentes:")

# Exibe a lista com opção de remover
for i, item in enumerate(st.session_state.lista):
    cols = st.columns([0.8, 0.2])
    cols[0].write(f"🔹 {item}")
    if cols[1].button("Remover", key=f"del_{i}"):
        st.session_state.lista.pop(i)
        salvar_dados(st.session_state.lista)
        st.rerun()

if not st.session_state.lista:
    st.info("Sua lista está vazia!")