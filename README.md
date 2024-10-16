# JAMProtect

**Versão:** 1.0  
**Desenvolvedor:** Jordan Adelino

## Descrição

O **JAMProtect** é um antivírus desenvolvido para detectar, prevenir e eliminar arquivos maliciosos em sistemas Windows. Ele foi especialmente projetado para uso em ambientes educacionais, como o Colégio Helvip, para garantir que os computadores estejam protegidos contra ameaças como malware, vírus de script (.js), e outros arquivos potencialmente perigosos.

## Funcionalidades

- **Escaneamento de sistema**: Detecta e remove arquivos maliciosos, baseados em padrões conhecidos.
- **Monitoramento de unidades USB**: Verifica automaticamente novas unidades conectadas e elimina arquivos suspeitos.
- **Limpeza de registro do Windows**: Remove entradas de registro maliciosas para garantir a segurança do sistema.
- **Autoinicialização**: O JAMProtect é configurado para ser executado automaticamente sempre que o sistema for iniciado.
- **Interface amigável**: Interface gráfica desenvolvida com Flet, permitindo fácil interação e visualização de logs de atividade.

## Instalação

### Requisitos

- Python 3.10 ou superior
- Bibliotecas necessárias (instaladas automaticamente via `requirements.txt`)

### Passos para instalação e execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/jamprotect.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd jamprotect
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Compile o executável usando o PyInstaller:
   ```bash
   pyinstaller jam.spec
   ```

5. O executável será gerado na pasta `dist/JAMProtect/`.

6. Copie o executável gerado (`JAMProtect.exe`) e o ícone (`assets/jamprotect.ico`) para a pasta de destino nas máquinas Windows do colégio.

7. Para configurar o JAMProtect para iniciar automaticamente com o sistema, o executável será movido para a pasta de inicialização:
   ```bash
   python autorun.py
   ```

## Uso

- Execute o **JAMProtect.exe** e clique no botão "Iniciar Verificação" para iniciar o escaneamento do sistema.
- Utilize o botão "Limpar Logs" para limpar o histórico de atividades.
- O programa vai monitorar automaticamente novas unidades USB conectadas e remover arquivos maliciosos quando detectados.

## Estrutura do Projeto

```bash
.
├── assets
│   └── jamprotect.ico  # Ícone do antivírus
├── jam
│   ├── logic.py        # Lógica de detecção e remoção de malware
│   ├── autorun.py      # Script para configurar a autoinicialização
├── main.py             # Interface do usuário (GUI) em Flet
├── jam.spec            # Arquivo de configuração do PyInstaller
├── README.md           # Este arquivo
└── requirements.txt    # Dependências do projeto
```

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).

---
