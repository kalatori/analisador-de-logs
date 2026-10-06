import sqlite3
conexao = sqlite3.connect("logs.db")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS eventos")
cursor.execute("""
    CREATE TABLE eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora TEXT,
        evento TEXT,
        usuario TEXT,
        ip TEXT
    )
""")

with open("acessos.log", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    linha = linha.strip()
    if linha == "":
        continue
    partes = linha.split(" ")
    data_hora = partes[0] + " " + partes[1]
    evento = partes[2]
    usuario = partes[3].replace("usuario=", "")
    ip = partes[4].replace("ip=", "")
    cursor.execute(
        "INSERT INTO eventos (data_hora, evento, usuario, ip) VALUES (?, ?, ?, ?)",
        (data_hora, evento, usuario, ip),
    )

conexao.commit()

cursor.execute("""
    SELECT ip, COUNT(*) AS total
    FROM eventos
    WHERE evento = 'LOGIN_FALHOU'
    GROUP BY ip
    HAVING COUNT(*) >= 3
    ORDER BY total DESC
""")

for ip, total in cursor.fetchall():
    print(f"ALERTA: o IP {ip} falhou {total} vezes!")

conexao.close()
