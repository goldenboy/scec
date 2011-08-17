# -*- coding: utf-8 -*-




db.define_table('bachiller_dato_plano',
    Field('di', 'integer'),
    Field('nombre1', 'string', length=64),
    Field('apellido1', 'string', length=64),
    Field('nombre2', 'string', length=64),
    Field('apellido2', 'string', length=64),
    Field('carrera', db.carrera),
    Field('modalidad_ingreso', db.modalidad_ingreso),
    Field('fecha_reg', 'date', default=request.now, writable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)



