# -*- coding: utf-8 -*-




db.define_table('bachiller',
    Field('di', 'integer'),
    Field('nombre', 'string', length=64),
    Field('apellido', 'string', length=64),
    Field('fecha_nac', 'date'),
    Field('nac', db.pais),
    Field('estado_civil', 'string', length=1),
    Field('sexo', 'string', length=1),
    Field('direccion', 'string', length=512),
    Field('tlf_fijo', 'string', length=64 ),
    Field('tlf_movil', 'string', length=64),
)




db.bachiller.nac.label = 'Nacionalidad'
db.bachiller.nac.requires = IS_IN_DB(db, 'pais.id', '%(nombre)s', zero='Seleccione el Pais')
db.bachiller.nac.comment = 'Nacionalidad'


db.bachiller.direccion.widget = SQLFORM.widgets.text.widget
