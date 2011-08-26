# -*- coding: utf-8 -*-


db.define_table('preinscripcion',
    Field('di', 'integer', writable=False, readable=False),
    Field('nombre1', 'string', length=64),
    Field('apellido1', 'string', length=64),
    Field('nombre2', 'string', length=64),
    Field('apellido2', 'string', length=64),
    Field('carrera', 'integer'),
    Field('modalidad_ingreso', 'string', length=1),
    Field('fecha_reg', 'date', default=request.now, writable=False, readable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)

