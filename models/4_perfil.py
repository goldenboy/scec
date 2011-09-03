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



db.define_table('perfil',
    Field('di', 'string', length=64, writable=False, readable=False),
    Field('email', 'string', length=128),
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
    Field('fecha_update', 'date', update=request.now, writable=False, readable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)

#requires
db.perfil.email.requires = IS_EMAIL()
db.perfil.nombre1.requires = db.perfil.nombre2.requires = db.perfil.apellido1.requires = db.perfil.apellido2.requires = _requires_nombre_apellido
db.perfil.estado_civil.requires = IS_IN_SET(_estado_civil)
db.perfil.sexo.requires = IS_IN_SET(_sexo)



db.perfil.direccion.requires = IS_NOT_EMPTY()
db.perfil.tlf_fijo.requires = db.perfil.tlf_movil.requires = [
    IS_LENGTH(minsize=10),
    IS_NOT_EMPTY()
]
db.perfil.tlf_fijo.comment = db.perfil.tlf_movil.comment = '02415553341'





