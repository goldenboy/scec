# -*- coding: utf-8 -*-

db.define_table('pais',
    Field('nombre', 'string', length=64),
    format = '%(nombre)s'
)



db.define_table('estado', #estado o region del pais
    Field('nombre', 'string', length=64),
    format='%(nombre)s'
)



db.define_table('historial',
    Field('evento', 'string'),
    Field('fecha_hora', 'datetime', default=request.now),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),    
)



db.define_table('carrera',
    Field('codigo', 'integer'), #obsoleto agregado para soporte del msin
    Field('nombre', 'string', length=64),
    Field('fecha_reg', 'date', default=request.now, writable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
    format = '%(codigo)s :: %(nombre)s'
)



db.define_table('modalidad_ingreso',
    Field('codigo', 'integer'), #obsoleto agregado para soporte del msin
    Field('nombre', 'string', length=64),
    Field('fecha_reg', 'date', default=request.now, writable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
    format = '%(codigo)s :: %(nombre)s'
)

