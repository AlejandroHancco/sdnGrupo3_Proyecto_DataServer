from flask import Flask, render_template
import multiprocessing

# ---------- Módulo del servidor en puerto 9000 ----------
def server_9000():
    app = Flask("server_9000", template_folder='templates')

    @app.route('/')
    def home():
        return render_template('page_9000.html')

    app.run(host='0.0.0.0', port=9000)

# ---------- Módulo del servidor en puerto 9001 ----------
def server_9001():
    app = Flask("server_9001", template_folder='templates')

    @app.route('/')
    def home():
        return render_template('circuitos.html')

    app.run(host='0.0.0.0', port=9001)

# ---------- Módulo del servidor en puerto 9002 ----------
def server_9002():
    app = Flask("server_9002", template_folder='templates')

    @app.route('/')
    def home():
        return render_template('tecom2.html')

    app.run(host='0.0.0.0', port=9002)

# ---------- Módulo del servidor en puerto 9003 ----------
def server_9003():
    app = Flask("server_9003", template_folder='templates')

    @app.route('/')
    def home():
        return render_template('ciber.html')

    app.run(host='0.0.0.0', port=9003)

# ---------- Módulo del servidor en puerto 9004 ----------
def server_9004():
    app = Flask("server_9004", template_folder='templates')

    @app.route('/')
    def home():
        return render_template('circuitos.html')

    app.run(host='0.0.0.0', port=9004)

# ---------- Iniciador de todos los servidores ----------
def start_all_servers():
    processes = [
        multiprocessing.Process(target=server_9000),
        multiprocessing.Process(target=server_9001),
        multiprocessing.Process(target=server_9002),
        multiprocessing.Process(target=server_9003),
        multiprocessing.Process(target=server_9004),
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

if __name__ == '__main__':
    start_all_servers()
