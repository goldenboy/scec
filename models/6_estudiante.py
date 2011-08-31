# -*- coding: utf-8 -*-


db.define_table('estudiante',
    Field('autorizado', db.auth_user, default=id_user, writable=False, readable=False),
    Field('fecha_reg', 'date', default=request.now, writable=False, readable=False),
    Field('fecha_update', 'date', update=request.now, writable=False, readable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)

