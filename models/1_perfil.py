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
    1:'root', #creado por el sistema 
    2:'tecnico_control_estudio', # cargado y asignado por root
    3:'director_control_estudio', # asignado por root (root activa o bloquea)
    4:'director_escuela', # asignado por root ademas de activa o bloquea

    5:'personal_control_estudio', # asignado por director control de estudios ademas de activa o bloquear 
    6:'estudiante', # asignado por director_control_estudio, (tecnico activa o bloquea)
    7:'profesor', # asignado por director_control_estudio (tecnico activa o bloquea)
    8:'coordinador_asignatura', # asignado por director_control_estudio (tecnico activa o bloquea)
}




_perfil_status = {
    'a':'Activo',
    'b':'Bloqueado',
    'c':'Activo con codigo nuevo'
}

_perfil_proceso = {
    1:'Iscripcion',
    2:'Ratificacion',
    3:'Muchos mas'
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
    Field('fecha_update', 'date', update=request.now, writable=False, readable=False),
    Field('tipo', 'list:integer', writable=False, readable=False),
    Field('status', 'string', length=1, default='c', writable=False, readable=False),
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
db.perfil.status.requires = IS_IN_SET(_perfil_status, zero=None)

db.perfil.direccion.requires = IS_NOT_EMPTY()
db.perfil.tlf_fijo.requires = db.perfil.tlf_movil.requires = [
    IS_LENGTH(minsize=10),
    IS_NOT_EMPTY()
]
db.perfil.tlf_fijo.comment = db.perfil.tlf_movil.comment = '02415553341'


db.perfil.tipo.represent = lambda v: [_perfil_tipo[tipo] + ' ' for tipo in v]






