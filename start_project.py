import os
import subprocess
import sys

def start_backend():
    print(" Iniciando servidor BACKEND...")
    os.chdir("backend")
    subprocess.Popen([sys.executable, "manage.py", "runserver"])
    os.chdir("..")

def start_frontend():
    print(" Iniciando servidor FRONTEND...")
    os.chdir("frontend")
    subprocess.Popen(["npm", "run", "start"], shell=True)
    os.chdir("..")

if __name__ == "__main__":
    print(" Inicializando servidores...")
    start_backend()
    start_frontend()
    print(" Tudo rodando! Acesse o navegador e veja a mágica acontecer ")
