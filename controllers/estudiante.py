# -*- coding: utf-8 -*-

def index():

    return dict()



@auth.requires( auth.has_membership('director') or auth.has_membership('decano'))
def add():

    
    form = SQLFORM.factory(
                Field('data', 'text')
            )
    
    if form.accepts(request.vars, session):
        response.flah = 'Datos cargados'

    return dict(form=form, carrera=carrera, modalidad_ingreso=modalidad_ingreso)





