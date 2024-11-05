import tkinter as tk
from tkinter import ttk
import requests

# Funções de consulta e cadastro

def consultar_placas():
    try:
        response = requests.get("http://127.0.0.1:5000/placas")  # Verifique a rota correta na API
        if response.status_code == 200:
            placas = response.json()
            lbl_resultado.config(text="\n".join(placas))  # Exibe as placas na mesma janela
        else:
            lbl_resultado.config(text="Não foi possível buscar as placas.")  # Exibe o erro na mesma janela
    except Exception as e:
        lbl_resultado.config(text="Erro de Conexão: " + str(e))  # Exibe erro de conexão na mesma janela

def cadastrar_placa(placa):
    try:
        response = requests.post("http://127.0.0.1:5000/cadastrar_placa", json={"placa": placa})
        if response.status_code == 201:
            lbl_resultado.config(text="Placa cadastrada com sucesso!")  # Exibe sucesso na mesma janela
        else:
            lbl_resultado.config(text="Não foi possível cadastrar a placa.")  # Exibe erro na mesma janela
    except Exception as e:
        lbl_resultado.config(text="Erro de Conexão: " + str(e))  # Exibe erro de conexão na mesma janela

def consultar_vagas_disponiveis():
    try:
        response = requests.get("http://127.0.0.1:5000/vagas_disponiveis")
        if response.status_code == 200:
            vagas = response.json()
            lbl_resultado.config(text=str(vagas))  # Exibe as vagas na mesma janela
        else:
            lbl_resultado.config(text="Não foi possível buscar as vagas.")  # Exibe erro na mesma janela
    except Exception as e:
        lbl_resultado.config(text="Erro de Conexão: " + str(e))  # Exibe erro de conexão na mesma janela

def consultar_permanencia_saldo(placa):
    try:
        response = requests.get(f"http://127.0.0.1:5000/tempo_e_saldo/{placa}")  # URL ajustada
        if response.status_code == 200:
            dados = response.json()
            permanencia = dados.get("data_entrada")  # Ajuste de chave para exibir a data de entrada
            saldo = dados.get("saldo")
            lbl_resultado.config(text=f"Tempo: {permanencia}\nSaldo: {saldo}")  # Exibe dados na mesma janela
        else:
            lbl_resultado.config(text="Não foi possível buscar os dados.")  # Exibe erro na mesma janela
    except Exception as e:
        lbl_resultado.config(text="Erro de Conexão: " + str(e))  # Exibe erro de conexão na mesma janela

def consultar_planos_fidelidade():
    # Planos mockados
    planos = [
        {"nome": "Estacionamento na Veia - Forte e Vingador", "beneficios": "Acesso ilimitado, estacionamento reservado, descontos exclusivos", "requisitos": "Pagamento mensal de R$ 200,00"},
        {"nome": "Estacionamento na Veia - Preto", "beneficios": "Acesso a vagas preferenciais, descontos em estacionamentos parceiros", "requisitos": "Pagamento mensal de R$ 120,00"},
        {"nome": "Estacionamento na Veia - Prata", "beneficios": "Descontos em estacionamentos parceiros", "requisitos": "Pagamento mensal de R$ 60,00"}
    ]
    
    # Gerando as informações para exibir
    planos_info = "\n".join([f"Plano: {p['nome']} - Benefícios: {p['beneficios']} - Requisitos: {p['requisitos']}" for p in planos])
    
    # Exibindo a informação dos planos na mesma janela
    lbl_resultado.config(text=planos_info)


# Configuração da interface principal com abas
root = tk.Tk()
root.title("Gerenciador do Estacionamento")
root.geometry("500x300")  # Define o tamanho da janela para 500x300

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Aba para Consulta e Cadastro de Placas (História 1)
frame_placas = ttk.Frame(notebook)
notebook.add(frame_placas, text="Consulta e Cadastro de Placas")

btn_consultar_placas = tk.Button(frame_placas, text="Consultar Placas", command=consultar_placas)
btn_consultar_placas.pack(pady=10)

tk.Label(frame_placas, text="Nova Placa:").pack(pady=5)
entry_nova_placa = tk.Entry(frame_placas)
entry_nova_placa.pack(pady=5)
btn_cadastrar_placa = tk.Button(frame_placas, text="Cadastrar Placa", command=lambda: cadastrar_placa(entry_nova_placa.get()))
btn_cadastrar_placa.pack(pady=10)

# Aba para Consulta de Vagas Disponíveis (História 2)
frame_vagas = ttk.Frame(notebook)
notebook.add(frame_vagas, text="Consulta de Vagas")
btn_consultar_vagas = tk.Button(frame_vagas, text="Consultar Vagas Disponíveis", command=consultar_vagas_disponiveis)
btn_consultar_vagas.pack(pady=10)

# Aba para Consulta de Tempo de Permanência e Saldo (História 3)
frame_permanencia = ttk.Frame(notebook)
notebook.add(frame_permanencia, text="Consulta de Permanência")
lbl_placa = tk.Label(frame_permanencia, text="Número da Placa:")
lbl_placa.pack(pady=5)
entry_placa = tk.Entry(frame_permanencia)
entry_placa.pack(pady=5)
btn_consultar_permanencia = tk.Button(frame_permanencia, text="Consultar Permanência e Saldo", command=lambda: consultar_permanencia_saldo(entry_placa.get()))
btn_consultar_permanencia.pack(pady=10)

# Aba para Consulta de Planos de Fidelidade (História 4)
frame_planos = ttk.Frame(notebook)
notebook.add(frame_planos, text="Consulta de Planos")
btn_consultar_planos = tk.Button(frame_planos, text="Consultar Planos de Fidelidade", command=consultar_planos_fidelidade)
btn_consultar_planos.pack(pady=10)

# Label para mostrar os resultados
lbl_resultado = tk.Label(frame_planos, text="", justify=tk.LEFT, anchor="w", font=("Arial", 10))
lbl_resultado.pack(pady=10, padx=10)

root.mainloop()
