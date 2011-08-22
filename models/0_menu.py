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


if auth.has_membership('root') or auth.has_membership('control_estudio'):
    response.menu += [
        ('Usuarios', False, URL('usuario','index'), 
            [
                ('Agregar', False, URL('usuario','add'), [])
            ])
    ]



if auth.has_membership('root'):
    response.menu += [
        ('Autoridad', False, URL('autoridad','index'), 
            [
                ('Agregar', False, URL('autoridad','add'), [])
            ])
    ]


if auth.has_membership('control_estudio') or auth.has_membership('autoridad'):
    response.menu += [
        ('Estudiantes', False, URL('estudiante','index'), 
            [
                ('Inscribir', False, URL('estudiante','add'), [])
            ])
    ]
