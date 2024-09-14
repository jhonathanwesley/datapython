# Git e GitHub
#### Uma introdução à versionamento de código e trabalho colaborativo
[Introdução - Aula 1: youtube.com](https://www.youtube.com/watch?v=napLViBKAtA&list=PLvlkVRRKOYFQ3cfYPjLeQ0KvrQ8bG5H11)

## Para que serve?
***
***É muito importante para:***

* versionamento de código / controle de versões
* backup / desfazer alterações
* colaboração / várias pessoas ao mesmo tempo em um mesmo projeto
* compartilhar código e o que está sendo construído

## O problema

- Como lidar com diversar alterações em seu projeto?
- Como tomar decisões que possam ser reversíveis?
- Como trabalhar com muitos constribuidores?
- Como distribuir?
---

### Git é um software
* Serve para gerenciamento de versão para arquivos de texto no computador.
* Criado por Linus Torvalds para melhorar o trabalho colaborativo em torno do Kernel do Linux.
* É **_Open-Source_** e poder ser instalado em qualquer sistema operacional.

> O Git permite criar **CHECKPOINTS** nos nossos projetos, para poder voltar em momentos anteriores a uma escolha, a um "nó" de código

## Comandos

### Git Bash 

* Bash permite falar diretamente com o sistema

1. `pwd` -> Mostra onde o terminal/você está
2. `ls` -> Mostra o que tem dentro do diretório/listar pastas e erquivos contidos no diretório
3. `cd` -> Ir para os diretórios, pastas, arquivos, navegar nos arquivos via comandos
  1. `cd` OneDrive [Vai para a pasta OneDrive]
  2. `cd` .. [Volta uma pasta|diretório]
  3. `cd ~` [Volta para a pasta raíz, pasta|diretório inicial]
  4. Após o `cd`, ao começar a escrever o nome de alguma pasta ou diretório pode ser usada a tecla `Tab` para autocomplete das pastas|diretórios
---
4. Como adicionar o versionamento no projeto | Como definir que ele será versionado pelo git:
  1. `git init .` -> Cria um novo repositório GIT
  2. `ls -a` -> Para mostrar todas as pastas (Incluindo as pastas ocultas)
  > Dentro de toda pasta existem pastas ocultas, a pasta `.` referencia a própria pasta e a `..` referencia a pasta hierarquicamente superior a pasta atual

5. `git status` -> Mostra a situação atual do seu projeto | branch atual
6. `git add <file name>` -> Seleciona o arquivo a ser salvo pelo git | Muda o arquivo do estado **UNSTAGED** para o estado **STAGED**
7. `git commit -m` -> Efetua o commit do arquivo | Checkpoint do arquivo [O `-m` serve para deixar uma mensagem]
  1. O `git commit` retornou um _'Author identity unknown'_, pediu uma identificação, pois é necessária uma identidade de autor para efetuar um `commit`
  2. Run

* `git config --global user.email "you@example.com"`
* `git config --global user.name "Your Name"`
* Só precisa ser definido uma vez, fica como identidade padrão
---
8. Agora, após realizar novamente o `git commit` o bash retorna o status atual do arquivo efetuado com sucesso
9. `git log` -> Mostra os registros | histórico dos commits
10. `git add .` -> Vai colocar todos os arquivos em **STAGED** para ser feito o `commit` (Tomar cuidado com ele, pois se houverem arquivos com informações sensíveis, eles serão enviados também)
11. `git reset` -> Retorna os arquivos atuais colocados em **STAGED** para **UNSTAGED**
12. `git reset idCommit` -> Retorna para o Pós-Commit
