# -*- coding: utf-8 -*-




db.define_table('estudiante',
    Field('fecha_reg', 'date', default=request.now, writable=False),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)


