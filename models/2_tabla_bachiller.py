# -*- coding: utf-8 -*-




db.define_table('bachiller',

    Field('user', db.auth_user, default=id_user, writable=False, readable=False),
)










