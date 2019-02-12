# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from datetime import datetime
from odoo import models
from odoo.exceptions import ValidationError

class Txoko(models.Model):
    _name = 'bote.txoko'
    direction = fields.Text(string="Direccion")
    name = fields.Char(string="Nombre")
    town = fields.Char(string="Ciudad")
    monthFee = fields.Float(string="Cuota Mensual")
    bote = fields.Float(string="Bote")
    idGastos = fields.One2many('bote.gasto', 'idTxoko', string="Gastos")
    admin_id = fields.Many2one('res.users', ondelete='cascade', string="Administradores del txoko")
    users_ids = fields.Many2many('res.users', string="Socios")
    
class Gasto(models.Model):
    _name = 'bote.gasto'
    date = fields.Datetime(string="Fecha", default=fields.datetime.now(), required=True)
    cantidad = fields.Integer(string="Cantidad", default="1", required=True)
    importe = fields.Float(string="Importe", required=True)
    idTxoko = fields.Many2one('bote.txoko', ondelete='cascade', string="Txoko", required=True,domain=[('bote','>',0.0)])
    idTipo = fields.Many2one('bote.tipogasto', ondelete='set null', string="Tipo de gasto", required=True)
    
    #@api.constrains('idTxoko')
    #def _only_admins_can_insert_expenses (self):
    #    for r in self:
    #        if r.idTxoko.admin_id == self.env.user:
    #            raise ValidationError("No eres admin")
    
    @api.onchange('cantidad')
    def _verify_cantidad(self):
        if self.cantidad <= 0:
            return{
                'warning': {
                    'title': "Incorrect",
                    'message': "Tiene que ser mayor que uno",
                },
            }
    @api.constrains('cantidad')
    def _cantidad_can_be_less_eq_zero(self):
        for r in self:
            if r.cantidad <= 0:
                raise ValidationError("Cantidad positiva")
            
    @api.onchange('date')
    def _verify_date(self):
        if datetime.strptime(self.date, '%Y-%m-%d %H:%M:%S') > fields.datetime.now():
            return{
                'warning': {
                    'title': "Incorrect",
                    'message': "La fecha tiene que ser menor o igual a la actual",
                },
            }
    @api.constrains('date')
    def _check_date_not_future(self):
        for r in self:
            if datetime.strptime(r.date, '%Y-%m-%d %H:%M:%S') > fields.datetime.now():
                raise ValidationError("La fecha tiene que ser menor o igual a la actual")        


class TipoGasto(models.Model):
    _name = 'bote.tipogasto'
    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripcion")
    idGastos = fields.One2many('bote.gasto', 'idTipo', string="Gastos")
    
class Users(models.Model):    
    _inherit = 'res.users'
    admin = fields.Boolean("Administrador de txoko", default=False)
    txoko_ids = fields.Many2many('bote.txoko', string="Txokos")
    admin_txokos_ids = fields.One2many('bote.txoko', 'admin_id', string="Administrador de")