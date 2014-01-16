#coding: utf-8
import MySQLdb

class ConexaoBanco:

    def conexao(self):
        con = MySQLdb.connect('','','','')
        con.autocommit(True)

        return con