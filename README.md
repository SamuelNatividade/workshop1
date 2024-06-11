# Workshop 1

## Sobre o Projeto

Esse repositorio faz parte do Workshop 1 da Jornada de Dados. Este projeto, tem como objetivo elucidar brevemente as ferramentas e libs necessárias para o desenvolvimento de um projeto de dados.

## Projeto

Esse projeto trata-se de um fluxo de ETL (Extract, Load e Transform) de dados de vários arquivos de excel, com o propósito de transformar-lo em um único arquivo.


## Início

#### Pré Requisitos

__VsCode__: Utilize o __Vscode__ configurado na sua máquina

__Git__ e __Github__: Configurados na sua máquina


## Instalacao e Configuracao

1. Clone o Repositorio

```bash
git clone https://github.com/SamuelNatividade/workshop1.git
```

2. Configure a versao correta do Python com o `pyenv`.

```bash
pyenvv install 3.11.3
pyenv local 3.11.3
```

3. Configurar o ```poetry``` e o ```Python``` e ativar o ambiente virtual
```bash
poetry env use 3.11.3
poetry shell
```

4. Instale as depedencias do Projeto
```bash
poetry install
```

5. Execute os testes para garantir que está tudo funcionando na pasta do projeto
```bash
pytest -v
```

6. Execute o comando para execucao da ETL
```bash
task run
```

8. Verifica a paste data/out


## Contato

Dúvidas e feedbacks

[Samuel Natividade](https://www.linkedin.com/in/samuel-natividade-455548b9/)
