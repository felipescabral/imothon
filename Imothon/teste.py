import logging
from cliente_dao import ClienteDao

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='IMothon.log',level=logging.INFO)
logging.info("Iniciando execucao do banco de dados")

conn = ClienteDao()

logging.info("Conexao criada")

# conn.autocommit(True)

logging.info("Autocommit concedido.")

conn.insertClient('Oliver', '242425', '321', 'drummond', '123987123', 'F')
logging.info("Query executada")