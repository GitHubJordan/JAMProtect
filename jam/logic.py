import os
import shutil
import winreg
import time

quarantine_folder = os.path.join(os.getcwd(), 'quarantine')
log_file = os.path.join(os.getcwd(), 'scan_log.txt')

malicious_files = ["Adobe.js", "Files.js"]

def write_to_log(message):
    """Escreve mensagens no arquivo de log"""
    with open(log_file, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def move_to_quarantine(file_path):
    """Move arquivos maliciosos para a pasta de quarentena"""
    if not os.path.exists(quarantine_folder):
        os.makedirs(quarantine_folder)
    shutil.move(file_path, quarantine_folder)

def scan_for_malware():
    """Função para escanear o sistema em busca de malware"""
    detected_malware = []
    # Verifica a pasta de inicialização
    startup_folder = os.path.expandvars(r"%appdata%\Microsoft\Windows\Start Menu\Programs\Startup")
    detected_malware += detect_and_remove_malware(startup_folder)
    
    # Verifica as unidades USB conectadas
    usb_drives = get_usb_drives()
    for drive in usb_drives:
        detected_malware += detect_and_remove_malware(drive)
    
    return detected_malware

def detect_and_remove_malware(directory):
    """Detecta e remove malware em um diretório específico"""
    detected_malware = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file in malicious_files:
                print(f"Malware detectado: {file} em {root}")
                write_to_log(f"Malware detectado: {file} em {root}")
                os.remove(os.path.join(root, file))
                detected_malware.append(os.path.join(root, file))
    return detected_malware

def get_usb_drives():
    """Lista todas as unidades USB conectadas"""
    drives = []
    for drive in range(ord('A'), ord('Z')+1):
        if os.path.exists(f'{chr(drive)}:\\'):
            drives.append(f'{chr(drive)}:\\')
    return drives

def clean_registry():
    """Limpa entradas maliciosas no registro do Windows"""
    try:
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Hidden", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "ShowSuperHidden", 0, winreg.REG_DWORD, 1)
            print("Registro limpo com sucesso.")
            write_to_log("Registro limpo com sucesso.")
    except Exception as e:
        print(f"Erro ao limpar o registro: {e}")
        write_to_log(f"Erro ao limpar o registro: {e}")
