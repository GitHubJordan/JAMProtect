import flet as ft
import os
import subprocess
import time
from jam.logic import scan_for_malware, write_to_log, move_to_quarantine

def main(page: ft.Page):
    page.title = "JAMProtect - Antivírus"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 600
    page.window.height = 400

    page.window.bgcolor = ft.colors.BLUE
    page.bgcolor = ft.colors.PRIMARY_CONTAINER
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.left = 400
    page.window.top = 200

    # Chama o autorun para instalar o antivírus na inicialização
    subprocess.call(['python', 'jam/autorun.py'])

    # Caixa de texto para exibir logs
    log_box = ft.TextField(
        label="Logs de Atividade",
        multiline=True,
        width=400,
        height=200,
        text_align=ft.TextAlign.LEFT,
        read_only=True,
    )

    # Função de escaneamento
    def run_scan(e):
        status_text.value = "Escaneando o sistema..."
        page.update()

        log_box.value += "Iniciando escaneamento...\n"
        write_to_log("Iniciando escaneamento...")
        time.sleep(1)  # Simulando tempo de escaneamento
        
        # Chamar a função de escaneamento
        malicious_files = scan_for_malware()

        if malicious_files:
            for file in malicious_files:
                log_box.value += f"Arquivo malicioso detectado: {file}\n"
                move_to_quarantine(file)  # Mover o arquivo para quarentena
                log_box.value += f"Arquivo {file} movido para a quarentena.\n"
                write_to_log(f"Arquivo malicioso detectado e movido para a quarentena: {file}")
        else:
            log_box.value += "Nenhuma ameaça encontrada.\n"
            write_to_log("Nenhuma ameaça encontrada.")

        status_text.value = "Escaneamento concluído."
        page.update()

    # Função para limpar os logs
    def clear_logs(e):
        log_box.value = ""
        page.update()

    # Interface principal
    title = ft.Text("JAMProtect - Antivírus", size=30, weight="bold")
    status_text = ft.Text("Sistema protegido", size=20)
    scan_button = ft.ElevatedButton(text="Iniciar Verificação", on_click=run_scan)
    clear_button = ft.ElevatedButton(text="Limpar Logs", on_click=clear_logs)

    # Adicionando os elementos à página
    page.add(
        title,
        ft.Divider(height=4, thickness=2, color='#ffffff'),
        status_text,
        scan_button,
        log_box,
        clear_button,
    )

# Iniciar a aplicação Flet
if __name__ == '__main__':
    ft.app(target=main)
