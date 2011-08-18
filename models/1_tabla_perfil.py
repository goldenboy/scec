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


_usuario_tipo = {
    'e':'estudiante',
    'p':'profesor',
    'c':'control_estudio',
    'a':'autoridad',
    'r':'root'
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
    Field('direccion', 'text', length=512),
    Field('tlf_fijo', 'string', length=64 ),
    Field('tlf_movil', 'string', length=64),
    Field('fecha_reg', 'date', default=request.now, writable=False, readable=False),
    Field('usuario_tipo', 'list:integer', writable=False, readable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)

db.perfil.estado_civil.requires = IS_IN_SET(_estado_civil)
db.perfil.sexo.requires = IS_IN_SET(_sexo)
db.perfil.usuario_tipo.requires = IS_IN_SET(_usuario_tipo, multiple=True)

