# -*- coding: utf-8 -*-


_estado_civil = {
    'c':'Casado',
    's':'Soltero',
    'd':'Divorciado',
    'b':'Concubinato',
    'v':'Viudo'
}

_sexo = {
    'f':'Femenino',
    'm':'Masculino'
}


_perfil_tipo = {
    'e':'Estudiante',
    'p':'Profesor',
    'c':'Control Estudio',
    'a':'Autoridad',
    'r':'root'
}


_perfil_status = {
    'a':'Activo',
    'b':'Bloqueado'
}

_perfil_proceso = {
    '1':'Iscripcion',
    '2':'Ratificacion',
    '3':'Muchos mas'
}

db.define_table('perfil',
    Field('codigo_seguridad', 'string', default= generar_codigo_seguridad, writable=False, readable=False),
    Field('di', 'integer', writable=False, readable=False),
    Field('nombre1', 'string', length=64),
    Field('apellido1', 'string', length=64),
    Field('nombre2', 'string', length=64),
    Field('apellido2', 'string', length=64),
    Field('fecha_nac', 'date'),
    Field('estado_civil', 'string', length=1),
    Field('sexo', 'string', length=1),
    Field('pais', db.pais),
    Field('estado', db.estado),
    Field('direccion', 'text', length=512),
    Field('tlf_fijo', 'string', length=64 ),
    Field('tlf_movil', 'string', length=64),
    Field('fecha_reg', 'date', default=request.now, writable=False, readable=False),
    Field('tipo', 'list:string', writable=False, readable=False),
    Field('status', 'string', length=1, default='a', writable=False, readable=False),
    Field('proceso', 'list:integer', writable=False, readable=False),
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
db.perfil.estado_civil.requires = IS_IN_SET(_estado_civil)
db.perfil.sexo.requires = IS_IN_SET(_sexo)
db.perfil.tipo.requires = IS_IN_SET(_perfil_tipo, multiple=True)
db.perfil.status.requires = IS_IN_SET(_perfil_status)

db.perfil.direccion.requires = IS_NOT_EMPTY()
db.perfil.tlf_fijo.requires = db.perfil.tlf_movil.requires = [
    IS_LENGTH(minsize=10),
    IS_NOT_EMPTY()
]
db.perfil.tlf_fijo.comment = db.perfil.tlf_movil.comment = '02415553341'

