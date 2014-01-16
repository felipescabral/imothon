#!/usr/bin/python
#coding: utf-8

from ladon.ladonizer import ladonize
from ladon.types.ladontype import LadonType
from ladon.compat import PORTABLE_STRING
import MySQLdb

class Agendamento(LadonType):
    cliente_id = int
    imovel_id = int
    observacoes = unicode

class UserService(object):

    @ladonize(PORTABLE_STRING,rtype=[Agendamento])
    def enviarAgendamento(self,idCorretor):
        listAgendamentos = []
        try:
            con = MySQLdb.connect('54.207.','XXX','XXX','imothon')
            con.autocommit(True)
            cursor = con.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM agendamentos WHERE id > %s ', idCorretor)
            #cursor.execute('SELECT * FROM agendamentos WHERE id > 0')
            agendamentos = cursor.fetchall()
            for agendamento in agendamentos:
                agendamentoUnit = Agendamento()
                agendamentoUnit.imovel_id = agendamento['imovel_id']
                agendamentoUnit.cliente_id = agendamento['pessoa_id']
                agendamentoUnit.observacoes = agendamento['observacoes']
                listAgendamentos.append(agendamentoUnit)
                del agendamentoUnit
        finally:
            con.close()
            del cursor
        return listAgendamentos
