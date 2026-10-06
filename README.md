# Analisador de Logs

Programa em Python que lê registros de login, guarda os eventos num banco SQLite e mostra, numa página web, quais IPs tiveram muitas falhas de login (um sinal típico de ataque de força bruta).

#demonstrção visual




<img width="807" height="841" alt="image" src="https://github.com/user-attachments/assets/3d7d0cc2-b8af-476c-ae92-1df90e2d5537" />


[Clique aqui para abrir o painel  [Clique aqui para abrir o painel](https://log-analiser.streamlit.app))


## O que o painel mostra

- Gráfico de barras com o número de falhas de login por IP
- Controle deslizante para escolher a partir de quantas falhas o IP vira alerta
- Alertas em vermelho para os IPs suspeitos
- Tabela com todos os eventos registrados

Os dados são fictícios: 333 eventos de um dia, com usuários normais que às vezes erram a senha e alguns IPs que tentam muitas senhas em sequência.

## Tecnologias

Python, SQL (SQLite), Streamlit e pandas.

## Como rodar no seu computador

Você precisa ter o Python 3 instalado (no Windows, marque a opção "Add python.exe to PATH" na instalação).

- **Windows:** baixe o ZIP do repositório, extraia e dê dois cliques em `rodar.bat`.
- **Outros sistemas:** abra o terminal na pasta do projeto e rode `python -m pip install -r requirements.txt`, depois `python -m streamlit run app.py`.

O painel abre no navegador, normalmente em `localhost:8501`.

## Arquivos do projeto

- `app.py`: o painel visual em Streamlit
- `logs_teste.db`: banco SQLite com os dados fictícios usados pelo painel
- `acessos.log`: exemplo pequeno de log em texto
- `passo6.py`: primeira versão do projeto, que lê o log em texto e cria um banco SQL
- `requirements.txt`: lista de bibliotecas necessárias
- `rodar.bat`: atalho para abrir o painel no Windows

## O que aprendi

- Ler e interpretar arquivos de log
- Contar eventos com dicionários e com SQL (`GROUP BY` e `HAVING`)
- Usar consultas parametrizadas para evitar SQL injection
- Criar um painel visual com Streamlit
- Escolher um limite de alerta: baixo demais gera alarmes falsos, alto demais deixa ataques passarem

