# encoding: utf8

import MySQLdb

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class ClienteDao(Singleton):
    def __init__(self):
        """
        Inits MySQL connection
        """
        self._connect()
        return


    def _connect(self):
        """
        Creates connection
        """
        self.connection = MySQLdb.connect(host="54.207.5.187", \
            user="", \
            passwd="", \
            db="imothon", \
            port=3306)
        self.connection.autocommit(True)
        return


    def _get_cursor(self):

        try:
            self.connection.ping()
        except:
            self._connect()
        return self.connection.cursor()


    def insertCliente(self, nome, sobrenome, cpf, sexo):
        try:
            query = "INSERT INTO clientes(nome, sobrenome, cpf, sexo) VALUES (%s, %s, %s, %s)"
            cursor = self._get_cursor()
            cursor.execute(query,(nome, sobrenome, cpf, sexo))
            cursor.close()
            self.closeConexao()
        finally:
            if self.connection is not None:
                self.connection.close()
        return

    def deleteCliente(self, idCliente):
        try:
            query = "DELETE FROM clientes WHERE id = %s"
            cursor = self._get_cursor()
            cursor.execute(query, id)
            cursor.close()
            self.closeConexao()
        finally:
            if self.connection is not None:
                self.connection.close()
        return

    def updateCliente(self, idCliente, nome, sobrenome, cpf, sexo):
        try:
            query = "UPDATE clientes SET nome = %s, sobrenome = %s, cpf = %s, sexo = %s WHERE id = %s"
            cursor = self._get_cursor()
            cursor.execute(query,(nome, sobrenome, cpf, sexo, idCliente))
            cursor.close()
            self.closeConexao()
        finally:
            if self.connection is not None:
                self.connection.close()
        return



