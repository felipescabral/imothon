import logging
from cliente_dao import ClienteDao
from ImoveisDao import ImoveisDao

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='IMothon.log',level=logging.INFO)
logging.info("Iniciando execucao do banco de dados")

conn = ClienteDao()
logging.info("Conexao criada com tabela Cliente")
conn.insertClient('Oliver', '242425', '321', 'drummond', '123987123', 'F')
logging.info("Insert na tabela Cliente feito com sucesso")


connImoveis = ImoveisDao()
connImoveis.insertImovel(1, 1, 1000, 1234, 5, 2, 999, 700, "Otimo apartamento, mas todo ferrado")