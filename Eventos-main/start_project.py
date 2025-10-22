import subprocess
import os
import sys
import shutil

VENV_DIR = os.path.join(os.getcwd(), "venv")
PYTHON_VENV = os.path.join(VENV_DIR, "Scripts", "python.exe") if sys.platform.startswith("win") else os.path.join(VENV_DIR, "bin", "python")
BACKEND_PATH = os.path.join(os.getcwd(), "Eventos-Backend")
FRONTEND_PATH = os.path.join(os.getcwd(), "Eventos-Frontend")

REQUIRED_PACKAGES = [
    "django",
    "djangorestframework",
    "django-cors-headers",
    "pillow",
    "qrcode"
]

def ensure_virtualenv():
    """Cria e ativa automaticamente o ambiente virtual, se não existir"""
    if not os.path.exists(VENV_DIR):
        print("⚙️ Criando ambiente virtual (venv)...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Ambiente virtual criado!\n")

    # Se o script atual não estiver sendo executado pelo Python do venv, reinicia dentro dele
    if os.path.normpath(sys.executable) != os.path.normpath(PYTHON_VENV):
        print("🔁 Recarregando script dentro do ambiente virtual...")
        subprocess.run([PYTHON_VENV, __file__])
        sys.exit(0)

def ensure_pip():
    print("🔍 Verificando instalação do pip...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
        print("✅ Pip encontrado!\n")
    except subprocess.CalledProcessError:
        print("⚙️ Pip não encontrado. Instalando...")
        subprocess.run([sys.executable, "-m", "ensurepip", "--upgrade"], check=True)
        print("✅ Pip instalado!\n")

def ensure_dependencies():
    print("🔍 Verificando dependências Python...")
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            print(f"⚙️ Instalando {package}...")
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
    print("✅ Todas as dependências instaladas!\n")

def run_backend():
    print("🚀 Iniciando BACKEND (Django)...")
    return subprocess.Popen([sys.executable, "manage.py", "runserver"], cwd=BACKEND_PATH)

def run_frontend():
    print("🎨 Iniciando FRONTEND (npm run dev)...")
    if not shutil.which("npm"):
        print("❌ npm não encontrado. Instale o Node.js antes de continuar.")
        sys.exit(1)
    shell_flag = sys.platform.startswith("win")
    return subprocess.Popen(["npm", "run", "dev"], cwd=FRONTEND_PATH, shell=shell_flag)

if __name__ == "__main__":
    print("\n🚧 Inicializando servidores...\n")

    try:
        ensure_virtualenv()
        ensure_pip()
        ensure_dependencies()

        backend = run_backend()
        frontend = run_frontend()

        print("\n🔥 Ambos os servidores estão rodando!")
        print("   ➜ Backend:  http://127.0.0.1:8000/")
        print("   ➜ Frontend: http://localhost:5173/\n")

        backend.wait()
        frontend.wait()

    except KeyboardInterrupt:
        print("\n🛑 Encerrando servidores...")
        backend.terminate()
        frontend.terminate()
        print("✅ Servidores finalizados com sucesso.")

    except Exception as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)
