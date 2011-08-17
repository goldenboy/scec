# -*- coding: utf-8 -*-


_sexo = {
    'f':'Femenino',
    'm':'Masculino'
}


_estado_civil = {
    'c':'Casado',
    's':'Soltero',
    'd':'Divorciado',
    'b':'Concubinato',
    'v':'Viudo'
}


_grupo_sang = {
    '1':'O+',
    '2':'A+',
    '3':'B+',
    '4':'AB+',
    '5':'O-',
    '6':'A-',
    '7':'B-',
    '8':'AB-',
}


_raza = {
    '1':'Caucásico',
    '2':'Afroamericano',
    '3':'Asiático',
}



db.define_table('perfil',
    Field('di', 'integer'),
    Field('nombre1', 'string', length=64),
    Field('apellido1', 'string', length=64),
    Field('nombre2', 'string', length=64),
    Field('apellido2', 'string', length=64),
    Field('fecha_nac', 'date'),
    Field('estado_civil', 'string', length=1),
    Field('sexo', 'string', length=1),
    Field('pais', db.pais),
    Field('estado', db.estado),
    Field('direccion', 'string', length=512),
    Field('tlf_fijo', 'string', length=64 ),
    Field('tlf_movil', 'string', length=64),
    Field('fecha_reg', 'date', default=request.now, writable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)



#requires
db.perfil.di.requires = [
    IS_INT_IN_RANGE(999999, 30000000),
    IS_NOT_IN_DB(db, 'perfil.di')
]

db.perfil.nombre1.requires = db.perfil.nombre2.requires = db.perfil.apellido1.requires = db.perfil.apellido2.requires = [
    IS_LENGTH(minsize=3),
    IS_NOT_EMPTY()
]



db.perfil.estado_civil.requires = IS_IN_SET(_estado_civil, zero='Seleccione el estado Civil')
db.perfil.sexo.requires = IS_IN_SET(_sexo, zero='Seleccione el Sexo')
db.perfil.pais.requires = IS_IN_DB(db, 'pais.id', '%(nombre)s', zero='Seleccione el Pais')
db.perfil.estado.requires = IS_IN_DB(db, 'estado.nombre', zero=None)
db.perfil.direccion.requires = IS_NOT_EMPTY()
db.perfil.tlf_fijo.requires = db.perfil.tlf_movil.requires = [
    IS_LENGTH(minsize=10),
    IS_NOT_EMPTY()
]

#widget
db.perfil.direccion.widget = SQLFORM.widgets.text.widget

#comment
db.perfil.tlf_fijo.comment = db.perfil.tlf_movil.comment = 'Debe incluir el Codigo'





