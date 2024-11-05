import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Funções de consulta para cada história

def consultar_placas():
    try:
        response = requests.get("http://127.0.0.1:5000/placas")
        if response.status_code == 200:
            placas = response.json()
            messagebox.showinfo("Placas Cadastradas", "\n".join(placas))
        else:
            messagebox.showerror("Erro", "Não foi possível buscar as placas.")
    except Exception as e:
        messagebox.showerror("Erro de Conexão", str(e))

def consultar_vagas_disponiveis():
    try:
        response = requests.get("http://127.0.0.1:5000/vagas_disponiveis")
        if response.status_code == 200:
            vagas = response.json()
            messagebox.showinfo("Vagas Disponíveis", "\n".join(vagas))
        else:
            messagebox.showerror("Erro", "Não foi possível buscar as vagas.")
    except Exception as e:
        messagebox.showerror("Erro de Conexão", str(e))

def consultar_permanencia_saldo(placa):
    try:
        response = requests.get(f"http://127.0.0.1:5000/permanencia?placa={placa}")
        if response.status_code == 200:
            dados = response.json()
            permanencia = dados.get("permanencia")
            saldo = dados.get("saldo")
            messagebox.showinfo("Tempo e Saldo", f"Tempo: {permanencia}\nSaldo: {saldo}")
        else:
            messagebox.showerror("Erro", "Não foi possível buscar os dados.")
    except Exception as e:
        messagebox.showerror("Erro de Conexão", str(e))

def consultar_planos_fidelidade():
    try:
        response = requests.get("http://127.0.0.1:5000/planos_fidelidade")
        if response.status_code == 200:
            planos = response.json()
            planos_info = "\n".join([f"Plano: {p['nome']} - Benefícios: {p['beneficios']} - Requisitos: {p['requisitos']}" for p in planos])
            messagebox.showinfo("Planos de Fidelidade", planos_info)
        else:
            messagebox.showerror("Erro", "Não foi possível buscar os planos.")
    except Exception as e:
        messagebox.showerror("Erro de Conexão", str(e))

# Configuração da interface principal com abas
root = tk.Tk()
root.title("Gerenciador do Estacionamento")
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Aba para Consulta de Placas (História 1)
frame_placas = ttk.Frame(notebook)
notebook.add(frame_placas, text="Consulta de Placas")
btn_consultar_placas = tk.Button(frame_placas, text="Consultar Placas", command=consultar_placas)
btn_consultar_placas.pack(pady=10)

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

root.mainloop()
