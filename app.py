from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Rota para cadastrar uma nova placa
@app.route('/cadastrar_placa', methods=['POST'])
def cadastrar_placa():
    data = request.json
    placa = data.get('placa')

    conn = sqlite3.connect('estacionamento.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Placas (placa) VALUES (?)", (placa,))
        conn.commit()
        return jsonify({'message': 'Placa cadastrada com sucesso!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Placa já cadastrada!'}), 409
    finally:
        conn.close()

# Rota para verificar vagas não ocupadas
@app.route('/vagas_disponiveis', methods=['GET'])
def vagas_disponiveis():
    conn = sqlite3.connect('estacionamento.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Vagas WHERE ocupada = 0")
    vagas = cursor.fetchall()
    conn.close()
    return jsonify(vagas)

# Rota para consultar tempo de permanência e saldo
@app.route('/tempo_e_saldo/<placa>', methods=['GET'])
def tempo_e_saldo(placa):
    conn = sqlite3.connect('estacionamento.db')
    cursor = conn.cursor()
    cursor.execute("SELECT data_entrada FROM Placas WHERE placa = ?", (placa,))
    resultado = cursor.fetchone()
    
    if resultado:
        data_entrada = resultado[0]
        # Aqui, você pode calcular o tempo de permanência e o saldo
        return jsonify({'data_entrada': data_entrada, 'saldo': 'calcular aqui'}), 200
    else:
        return jsonify({'message': 'Placa não encontrada!'}), 404

# Rota para consultar planos de fidelidade
@app.route('/planos', methods=['GET'])
def planos():
    conn = sqlite3.connect('estacionamento.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Planos")
    planos = cursor.fetchall()
    conn.close()
    return jsonify(planos)

if __name__ == '__main__':
    app.run(debug=True)
