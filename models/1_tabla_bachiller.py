# -*- coding: utf-8 -*-




db.define_table('bachiller',
    Field('di', 'integer'),
    Field('nombre', 'string', length=64),
    Field('apellido', 'string', length=64),
    Field('fecha_nac', 'date'),
    Field('nac', db.pais),
    Field('estado_civil', 'string', length=1),
    Field('sexo', 'string', length=1),
    Field('estado', db.estado),
    Field('direccion', 'string', length=512),
    Field('tlf_fijo', 'string', length=64 ),
    Field('tlf_movil', 'string', length=64),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)

db.bachiller.di.requires = IS_INT_IN_RANGE(999999, 30000000)
db.bachiller.nombre.requires = db.bachiller.apellido.requires = [
    IS_LENGTH(minsize=3),
    IS_NOT_EMPTY()
]

db.bachiller.nac.label = 'Nacionalidad'
db.bachiller.nac.requires = IS_IN_DB(db, 'pais.id', '%(nombre)s', zero='Seleccione el Pais')

db.bachiller.sexo.requires = IS_IN_SET(_sexo, zero='Seleccione el Sexo')


db.bachiller.estado.requires = IS_IN_DB(db, 'estado.nombre', zero='Solo aplica a Venezuela')

db.bachiller.direccion.requires = IS_NOT_EMPTY()
db.bachiller.direccion.widget = SQLFORM.widgets.text.widget

db.bachiller.tlf_fijo.comment = db.bachiller.tlf_movil.comment = 'Debe incluir el Codigo'
db.bachiller.tlf_fijo.requires = db.bachiller.tlf_movil.requires = [
    IS_LENGTH(minsize=10),
    IS_NOT_EMPTY()
]







