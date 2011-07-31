# -*- coding: utf-8 -*-




db.define_table('perfil',
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
    Field('fecha_reg', 'date', default=request.now, writable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)



db.perfil.di.requires = [
    IS_INT_IN_RANGE(999999, 30000000),
    IS_NOT_IN_DB(db, 'perfil.di')
]

db.perfil.nombre.requires = db.perfil.apellido.requires = [
    IS_LENGTH(minsize=3),
    IS_NOT_EMPTY()
]


db.perfil.nac.label = 'Nacionalidad'
db.perfil.nac.requires = IS_IN_DB(db, 'pais.id', '%(nombre)s', zero='Seleccione el Pais')


db.perfil.estado_civil.requires = IS_IN_SET(_estado_civil, zero='Seleccione el estado Civil')


db.perfil.sexo.requires = IS_IN_SET(_sexo, zero='Seleccione el Sexo')


db.perfil.estado.requires = IS_IN_DB(db, 'estado.nombre', zero=None)


db.perfil.direccion.requires = IS_NOT_EMPTY()
db.perfil.direccion.widget = SQLFORM.widgets.text.widget


db.perfil.tlf_fijo.comment = db.perfil.tlf_movil.comment = 'Debe incluir el Codigo'
db.perfil.tlf_fijo.requires = db.perfil.tlf_movil.requires = [
    IS_LENGTH(minsize=10),
    IS_NOT_EMPTY()
]





