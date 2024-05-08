import pyodbc
from datetime import date, timedelta
import locale

def conecta_ao_banco(driver='ODBC Driver 17 for SQL Server', server='xxx.xxx.xxx.xxx', database='DataBase', username='username', password='password', trusted_connection='no'):

    string_conexao = f"DRIVER={driver}; SERVER={server}; DATABASE={database}; UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor

conexao, cursor = conecta_ao_banco()

hoje = date.today()

visitantes_parque = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_catraca WHERE dh_inclusao BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND fk_atracao ='6';").fetchone()

visitantes_plataforma = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_catraca WHERE dh_inclusao BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND fk_atracao ='7';").fetchone()

visitantes_abusado = cursor.execute(f"SELECT COUNT(PK_ID) FROM pq_catraca WHERE dh_inclusao BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND fk_atracao ='8';").fetchone()

a = visitantes_parque[0]
b = visitantes_plataforma[0]
c = visitantes_abusado[0]

pagantes_parque = cursor.execute(f"SELECT COUNT(pk_id) FROM vw_catraca WHERE dh_catraca BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND tg_inativo = '0' AND nr_utilizacao = '1' AND vl_precoutilizacao > '1' AND cd_catraca != '2' AND cd_catraca != '0';").fetchone()

pp = pagantes_parque[0]

fat_ing = cursor.execute(f"SELECT SUM(vl_precoutilizacao) FROM vw_catraca WHERE dh_catraca BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND tg_inativo = '0' AND nr_utilizacao = '1' AND cd_catraca != '0';").fetchone()

faturamento_ingressos = fat_ing[0]
if faturamento_ingressos == None:
    faturamento_ingressos = 0

fat_est = cursor.execute(f"SELECT SUM(vl_precoutilizacao) FROM ( SELECT DISTINCT pk_id, vl_precoutilizacao FROM vw_catraca WHERE dh_catraca between '{hoje} 00:00:00'and '{hoje} 23:59:59' and tg_inativo = '0' and nr_utilizacao = '1' and nr_passaporte LIKE '6%') subconsulta;").fetchone()

faturamento_estacionamento = fat_est[0]
if faturamento_estacionamento == None:
    faturamento_estacionamento = 0

caixa_store01 = cursor.execute(f"SELECT SUM(vl_total) FROM pv_financeiro WHERE tg_origem = 'V' AND dt_emissao BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND fk_owner = '34';").fetchone()
caixa_store02 = cursor.execute(f"SELECT SUM(vl_total) FROM pv_financeiro WHERE tg_origem = 'V' AND dt_emissao BETWEEN '{hoje} 00:00:00' AND '{hoje} 23:59:59' AND fk_owner = '35';").fetchone()

cs01 = caixa_store01[0]
if cs01 == None:
    cs01 = 0
cs02 = caixa_store02[0]
if cs02 == None:
    cs02 = 0
faturamento_loja = cs01 + cs02

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

fi = locale.format_string('%.2f', faturamento_ingressos, grouping=True)
fe = locale.format_string('%.2f', faturamento_estacionamento, grouping=True)
fl = locale.format_string('%.2f', faturamento_loja, grouping=True)


dt1 = hoje + timedelta(days=1)
dt2 = hoje + timedelta(days=2)
dt3 = hoje + timedelta(days=3)
dt4 = hoje + timedelta(days=4)
dt5 = hoje + timedelta(days=5)

previs0 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{hoje} 00:00:00' AND tg_inativo = '0' AND vl_preuni > '1' AND fk_produto IN (SELECT pk_id FROM tb_produtos WHERE TG_VISITANTE = '1');").fetchone()
previs1 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt1} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs2 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt2} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs3 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt3} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs4 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt4} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()
previs5 = cursor.execute(f"SELECT COUNT(pk_id) FROM pq_ingresso WHERE dt_previsaovisita = '{dt5} 00:00:00' AND tg_inativo = '0' AND vl_preuni != '0';").fetchone()

p0 = previs0[0]
p1 = previs1[0]
p2 = previs2[0]
p3 = previs3[0]
p4 = previs4[0]
p5 = previs5[0]


print("NÃO FECHAR!!!")
