# -*- coding: utf-8 -*-




db.define_table('socio_e',
    Field('dato_x', 'string'),
    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)










