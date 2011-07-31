# -*- coding: utf-8 -*-

db.define_table('baciller',
    Field('di', 'integer'),
    Field('nombre', 'string', length=64),
    Field('apellido', 'string', length=64),
    Field('fecha_nac', 'date'),
    Field('estado_civil', 'string', length=1),
    Field('sexo', 'string', length=1),
    Field('direccion', 'string', length=512),
    Field('tlf_fijo', 'string', length=64 ),
    Field('tlf_movil', 'string', length=64),
)
