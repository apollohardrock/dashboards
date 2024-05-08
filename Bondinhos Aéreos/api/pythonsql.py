import pyodbc
from datetime import date, timedelta
import locale

# Parâmetros da conexão
driver = '{FreeTDS}'
server = 'server, port' 
database = 'DataBase' 
username = 'username' 
password = 'password' 

# String de conexão
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Estabelecendo a conexão
conn = pyodbc.connect(conn_str)

# Criando um cursor
cursor = conn.cursor()

# Definindo a data
hoje = date.today()

# Variáveis de datas
dt1 = hoje + timedelta(days=1)
dt2 = hoje + timedelta(days=2)
dt3 = hoje + timedelta(days=3)
dt4 = hoje + timedelta(days=4)
dt5 = hoje + timedelta(days=5)

# Extraindo dados do banco de dados
visitantes_bondinho = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_catraca WHERE cd_catraca = 1 AND dh_inclusao BETWEEN '{hoje} 00:00:00.000' and '{hoje} 23:59:59.999';").fetchone()
visitantes_eagle = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_catraca WHERE cd_catraca = 3 AND dh_inclusao BETWEEN '{hoje} 00:00:00.000' and '{hoje} 23:59:59.999';").fetchone()

pagantes_parque = cursor.execute(f"SELECT COUNT(pk_id) FROM vw_catraca WHERE dh_catraca BETWEEN '{hoje} 00:00:00.000' AND '{hoje} 23:59:59.999' AND tg_inativo = '0' AND nr_utilizacao = '1' AND vl_precoutilizacao > '1' AND cd_catraca = '1';").fetchone()

previs0 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{hoje} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs1 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt1} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs2 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt2} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs3 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt3} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs4 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt4} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs5 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt5} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()

faturamento_ingressos = cursor.execute(f"SELECT SUM(vl_precoutilizacao) from vw_catraca WHERE dh_catraca BETWEEN '{hoje} 00:00:00.000' AND '{hoje} 23:59:59.999' AND tg_inativo = '0' AND nr_utilizacao = '1';").fetchone()

# Variáveis valor visitantes
vb = visitantes_bondinho[0]
ve = visitantes_eagle[0]

pp = pagantes_parque[0]

p0 = previs0[0]
p1 = previs1[0]
p2 = previs2[0]
p3 = previs3[0]
p4 = previs4[0]
p5 = previs5[0]

# Declarando valor inicial da variável
fat_ing = faturamento_ingressos[0]
if fat_ing == None:
    fat_ing = 0

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Variáveis de valores
fi = locale.format_string('%.2f', fat_ing, grouping=True)


print ("NAO FECHAR!!!")
