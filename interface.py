import tkinter as tk
import requests

def cadastrar_placa():
    placa = placa_entry.get()
    response = requests.post('http://127.0.0.1:5000/cadastrar_placa', json={'placa': placa})
    result_label['text'] = response.json().get('message')

def consultar_vagas():
    response = requests.get('http://127.0.0.1:5000/vagas_disponiveis')
    vagas = response.json()
    result_label['text'] = f'Vagas disponíveis: {vagas}'

def consultar_planos():
    response = requests.get('http://127.0.0.1:5000/planos')
    planos = response.json()
    result_label['text'] = f'Planos disponíveis: {planos}'

# Interface Gráfica
window = tk.Tk()
window.title("Estacionamento")

# Cadastro de Placa
tk.Label(window, text="Placa do Veículo:").pack()
placa_entry = tk.Entry(window)
placa_entry.pack()
tk.Button(window, text="Cadastrar Placa", command=cadastrar_placa).pack()

# Consultar Vagas
tk.Button(window, text="Consultar Vagas Disponíveis", command=consultar_vagas).pack()

# Consultar Planos
tk.Button(window, text="Consultar Planos de Fidelidade", command=consultar_planos).pack()

# Resultado
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
