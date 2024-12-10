import streamlit as st
import pandas as pd

# Dados iniciais (você pode carregar de um banco de dados ou arquivo)
data = {
    "ID": [1, 2, 3],
    "Nome": ["Alice", "Bob", "Carol"],
    "Cargo": ["Analista", "Gerente", "Técnico"]
}

# Converta para DataFrame
df = pd.DataFrame(data)

# Título da aplicação
st.title("Gerenciador de Lista de Funcionários")

# Mostrando a tabela
st.subheader("Lista Atual de Funcionários")
st.dataframe(df)

# Adicionar novo funcionário
st.subheader("Adicionar Funcionário")
with st.form("add_employee_form"):
    new_id = st.number_input("ID", min_value=1, step=1)
    new_name = st.text_input("Nome")
    new_role = st.text_input("Cargo")
    submitted = st.form_submit_button("Adicionar")

    if submitted:
        # Adicionar o novo funcionário ao DataFrame
        new_data = pd.DataFrame({"ID": [new_id], "Nome": [new_name], "Cargo": [new_role]})
        df = pd.concat([df, new_data], ignore_index=True)
        st.success("Funcionário adicionado com sucesso!")

# Remover funcionário
st.subheader("Remover Funcionário")
remove_id = st.number_input("ID do Funcionário a Remover", min_value=1, step=1)
if st.button("Remover"):
    if remove_id in df["ID"].values:
        df = df[df["ID"] != remove_id]
        st.success("Funcionário removido com sucesso!")
    else:
        st.warning("ID não encontrado!")

# Editar funcionário (simples exemplo)
st.subheader("Editar Funcionário")
edit_id = st.number_input("ID do Funcionário a Editar", min_value=1, step=1)
if st.button("Editar"):
    if edit_id in df["ID"].values:
        selected_row = df[df["ID"] == edit_id]
        st.write("Funcionário selecionado:", selected_row)
        new_name = st.text_input("Novo Nome", selected_row["Nome"].values[0])
        new_role = st.text_input("Novo Cargo", selected_row["Cargo"].values[0])
        if st.button("Salvar Alterações"):
            df.loc[df["ID"] == edit_id, "Nome"] = new_name
            df.loc[df["ID"] == edit_id, "Cargo"] = new_role
            st.success("Dados atualizados com sucesso!")
    else:
        st.warning("ID não encontrado!")

# Salvar as alterações
st.subheader("Salvar Alterações")
if st.button("Salvar Lista"):
    df.to_csv("lista_funcionarios.csv", index=False)
    st.success("Lista salva com sucesso em 'lista_funcionarios.csv'!")
