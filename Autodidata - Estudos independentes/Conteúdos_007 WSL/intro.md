# Usar WSL 2

### Abrindo o projeto no UBUNTU com o VS Code da forma correta
> Abrir o terminal Ubuntu:

- Digitar o comando para abrir um projeto com o VS Code: code nome_da_pasta_do_projeto
    -Ex.: code datapython/

- Instalar pacotes / módulos / bibliotecas python como administrador:
- Com `SUDO APT`
    - `sudo apt install python3-nome_do_pacote`
- Com `PIPX`
    - `sudo apt install pipx`

---
## Criar ambiente virtual Ubuntu
- No terminal do WSL, execute o comando abaixo para garantir que o Python 3 está instalado:

 `sudo apt install python3-venv`

- Se não estiver instalado, você pode instalá-lo com:

`
sudo apt update
sudo apt install python3 python3-venv python3-pip
`

- Navegue até o diretório onde deseja criar o ambiente virtual:

`cd /caminho/para/o/diretorio`

- Crie o ambiente virtual com o seguinte comando:

`python3 -m venv nome_do_ambiente`

- Ative o ambiente com o seguinte comando:

`source nome_do_ambiente/bin/activate`

- Para **desativar / sair** do ambiente virtual, basta executar o comando:

`deactivate`

- **Para abrir no VS Code:**

- `code nome_do_ambiente`

---
### Estrutura recomendada de ambiente para cada projeto:

projeto/

│

├── venv/               # Diretório do ambiente virtual (mantém pacotes instalados)

│

├── .git/               # Diretório do Git (informações de controle de versão)

│

├── requirements.txt    # Arquivo com as dependências do projeto

├── main.py             # Código fonte

├── notebooks/          # Diretório com Jupyter Notebooks

└── README.md           # Arquivo de documentação

---
## Remover pastas / diretórios
- Navegue até o diretório onde a pasta está localizada, se necessário, usando o comando cd. Por exemplo:

`cd /caminho/para/a/pasta`

- Para deletar a pasta, use o seguinte comando:

`rm -rf nome-da-pasta`
