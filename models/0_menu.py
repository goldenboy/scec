# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = 'Sistema de Control de Estudios'
response.subtitle = 'Propotipo'

#http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Luis Diaz'
response.meta.description = ''
response.meta.keywords = ''
response.meta.generator = ''
response.meta.copyright = ''


##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    ('Home/Noticias', False, URL('default','index'), [])
    ]

_perfil_dato_basico = ('Datos Basicos', False, URL('default','index'), [])
_perfil_se = ('Dato Socio Economico', False, URL('default','index'), [])


response.menu += [
    ('Personal', False, '#', 
        [
            ('Perfil', False, URL('default','index'), [_perfil_dato_basico, _perfil_se]),
        ])
    ]


response.menu += [
    ('Inscripcion', False, URL('default','index'), [])
    ]


response.menu += [
    ('Inscripcion', False, URL('default','index'), [])
    ]


