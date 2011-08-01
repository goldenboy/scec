# -*- coding: utf-8 -*-



# formato del archivo del banco
# sin cabezera
# datos entre comillas dobles
# fecha, numero deposito o factura, monto
# ejemplo:
# "01/07/2011","0329135068310","2076.92"

db.define_table('archivo_cuenta',
    Field('descripcion', 'string', length=512),
    Field('archivo', 'upload', autodelete=True),
    Field('fecha_reg', 'date', default=request.now, writable=False, readable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
    format = '%(fecha_reg)s - %(descripcion)s'
)

#segudidad
db.archivo_cuenta.archivo.authorization = lambda record: \
    auth.is_logged_in() and \
    auth.has_permission('read', db.archivo_cuenta, record.id, auth.user.id)


#widget
db.archivo_cuenta.descripcion.widget = SQLFORM.widgets.text.widget




db.define_table('archivo_cuenta_desglosado',
    Field('archivo_cuenta', db.archivo_cuenta),
    Field('fecha', 'date'),
    Field('numero', 'integer'),
    Field('monto','decimal(9,2)'),
    Field('fecha_reg', 'date', default=request.now, writable=False, readable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)





db.define_table('forma_pago',
    Field('nombre', 'string', length=64),
    format = '%(nombre)s'
)

_pago_forma = {
    'd':'Deposito',
    'e':'Efectivo'
}


db.define_table('pago',
    Field('numero', 'integer'), #numero de deposito o recibo
    Field('forma_pago', 'string', length=1),
    Field('monto', 'decimal(9,2)'),
    Field('fecha', 'date'),
    Field('fecha_reg', 'date', default=request.now, writable=False, readable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)


#requeridos
db.pago.monto.requires = IS_DECIMAL_IN_RANGE(1,999999)
db.pago.forma_pago.requires = IS_IN_SET(_pago_forma, zero='Seleccione forma de Pago')


#comentario
db.pago.numero.comment = 'Numero de Deposito o Factura'





