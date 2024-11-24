from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def renderizar_html():
    return render_template('index.html')

@app.route('/monitor')
def monitor():
    # Exemplo de dados do sistema
    cpu = f"{psutil.cpu_percent(interval=1):.0f}" # % de cpu

    memory = f"{psutil.virtual_memory().percent:.0f}" # % de memoria usada
    memoria_total = f"{psutil.virtual_memory().total/1024**3:.0f}" # memoria total

    disk = f"{psutil.disk_usage('/').percent:.0f}" # % de disco usada
    disco_total =  f"{psutil.disk_usage('/').total/1024**3:.0f}" # disco total

    bateria = psutil.sensors_battery().percent # % de bateria

    return jsonify(cpu=cpu, memory=memory, memoria_total = memoria_total, disk=disk, disco_total= disco_total, bateria=bateria)

if __name__ == '__main__':
    app.run(debug=True)
