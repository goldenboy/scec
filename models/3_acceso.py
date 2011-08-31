# -*- coding: utf-8 -*-


_acceso_nivel = {
    1:'root', #creado por el sistema 
    2:'tecnico_control_estudio', # cargado y asignado por root
    3:'director_control_estudio', # asignado por root (root activa o bloquea)
    4:'director_escuela', # asignado por root ademas de activa o bloquea

    5:'personal_control_estudio', # asignado por director control de estudios ademas de activa o bloquear 
    6:'estudiante', # asignado por director_control_estudio, (tecnico activa o bloquea)
    7:'profesor', # asignado por director_control_estudio (tecnico activa o bloquea)
    8:'coordinador_asignatura', # asignado por director_control_estudio (tecnico activa o bloquea)
    99:'sin asignar'
}

_acceso_status = {
    'a':'Activo',
    'b':'Bloqueado',
    'c':'Activo con codigo nuevo'
}
db.define_table('acceso',
    Field('codigo_seguridad', 'string', default= generar_codigo_seguridad, writable=False, readable=False),
    Field('nivel', 'list:integer'),
    Field('status', 'string', length=1, default='c', writable=False, readable=False),
    Field('fecha_update', 'date', update=request.now, writable=False, readable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)

db.acceso.nivel.requires = IS_IN_SET(_acceso_nivel, zero=None)
db.acceso.status.requires = IS_IN_SET(_acceso_status, zero=None)

