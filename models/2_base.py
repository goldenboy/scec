# -*- coding: utf-8 -*-



db.define_table('pais',
    Field('nombre', 'string', length=64),
    format = '%(nombre)s'
)



db.define_table('estado', #estado o region del pais
    Field('nombre', 'string', length=64),
    format='%(nombre)s'
)




db.define_table('carrera',
    Field('codigo', 'string', length=10), #obsoleto agregado para soporte del msin
    Field('nombre', 'string', length=64),
    format = '%(codigo)s :: %(nombre)s'
)



db.define_table('modalidad_ingreso',
    Field('codigo', 'string', length=10), #obsoleto agregado para soporte del msin
    Field('nombre', 'string', length=64),
    format = '%(codigo)s :: %(nombre)s'
)




db.define_table('carrera_etapa',
    Field('carrera', db.carrera),
    Field('nombre', 'string', length=64),
    format = '%(nombre)s'
)




db.define_table('materia',
    Field('codigo', 'string', length=10), #obsoleto agregado para soporte del msin
    Field('nombre', 'string', length=64),
    Field('descripcion', 'string', length=512),
    Field('nota_minima', 'decimal(2,2)'),#nota minima aprovatoria
    Field('carrera', db.carrera),
    Field('carrera_etapa', db.carrera_etapa),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
    format = '%(codigo)s :: %(nombre)s'
)











