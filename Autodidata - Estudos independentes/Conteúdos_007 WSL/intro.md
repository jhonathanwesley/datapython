---
# Usar WSL 2
---
## Ativação WSL e instalação do Linux

- Para ativar o WSL no windows:
    - **Painel de Controle**
    - **Programas**
    - **Ativar ou Desativar recursos do Windows**
        - Ativar as seguintes opções:
            - _Plataforma de Máquina Virtual_
            - _Plataforma do Hivervisor do Windows_
            - _Subsistema do Windows para Linux_ (`WSL`)

> Reiniciar a máquina

- Após ativar o WSL, para verificar as distribuições linux disponíveis, abrir o terminal `Power Shell` ou `Windows Terminal` e digitar:

`wsl -l --online`

- Escolher a distro desejada, comando para instalar:

`wsl --install Ubuntu`

- Se a instalação for bem sucedida vai solicitar um nome de usuário e uma senha:

> Defina seu usuário e senha

`user`
`password`
`password`

- Com isso é possível usar o terminal da distribuição instalada

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

---
## Arquivo requirements.txt

- Se você quiser que outras pessoas (ou você mesmo em outro momento) possam instalar as mesmas dependências do ambiente, pode gerar um arquivo requirements.txt com todas as dependências instaladas no ambiente:

`pip freeze > requirements.txt`

- E para instalar essas dependências em outro ambiente (ou no mesmo, mas após deletá-lo e recriá-lo):

`pip install -r requirements.txt`

- O requirements.txt não é atualizado automaticamente.
- Sempre que instalar novos pacotes ou atualizar pacotes existentes, você precisará rodar o comando `pip freeze > requirements.txt` para manter o arquivo atualizado com as versões corretas.
