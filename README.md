# Simulador Circuitos Digitais

O **Simulador Circuitos Digitais** é uma ferramenta interativa para simular os sistemas físicos propostos em laboratórios de circuitos digitais. Este projeto está em estágio de desenvolvimento, e alguns recursos ainda estão sendo implementados.

## Requisitos
- **Python:** 3.12.1 ou superior. Baixe a versão mais recente no [site do python](https://www.python.org/downloads/).

### Dependências
- **Interface gráfica:** PySide6 6.8.0 ou superior.

## Usando o programa

Siga estas etapas para rodar o programa:

1. **Configure um ambiente virtual (opcional, mas recomendado):** Leia como criar um ambiente virtual [aqui](https://docs.python.org/3/library/venv.html).

2. **Instale as dependências:**

    No terminal, navegue até a pasta do projeto e execute:  
    ~~~bash
    pip install -r requirements.txt
     ~~~

3. **Execute o programa:**
    ~~~
    python main.py
    ~~~

## Compilando com nuitka
**O Nuitka é usado para criar um executável do programa, permitindo que ele seja executado sem a necessidade de Python instalado.**

1. **Instale as dependências para a compilação:**

    No terminal, navegue até a pasta do projeto e execute:  
    ~~~bash
    pip install -r requirements-build.txt
     ~~~

2. **Compile o executável:**
 
    ~~~bash
    python build.py
     ~~~

3. **O executável estará disponível na pasta**
    ~~~
    <pasta-do-projeto>/.output/main.dist/
    ~~~