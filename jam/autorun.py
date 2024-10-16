import os
import shutil

def install_autorun():
    """Instala o antivírus para ser executado na inicialização"""
    startup_folder = os.path.expandvars(r"%appdata%\Microsoft\Windows\Start Menu\Programs\Startup")
    antivirus_exe = os.path.join(os.getcwd(), 'JAMProtect.exe')

    if not os.path.exists(os.path.join(startup_folder, 'JAMProtect.exe')):
        shutil.copy(antivirus_exe, startup_folder)
        print("Antivírus configurado para iniciar com o sistema.")
    else:
        print("O antivírus já está configurado para iniciar com o sistema.")

if __name__ == '__main__':
    install_autorun()