# -*- coding: utf-8 -*-

def index():
    return dict()



def add_1():

    

    form = SQLFORM.factory(
                Field('data', 'text'),
                db.bachiller_dato_plano.carrera, 
            )
    carrera_sql = db(db.carrera.id>0).select()
    carrera = SQLTABLE( carrera_sql, headers={'carrera.codigo':'Codigo','carrera.nombre':'Carrera'}, columns = ['carrera.codigo','carrera.nombre'] )
    
    modalidad_ingreso_sql = db(db.modalidad_ingreso.id>0).select()
    modalidad_ingreso = SQLTABLE( modalidad_ingreso_sql, headers={'modalidad_ingreso.codigo':'Codigo', 'modalidad_ingreso.nombre':'Modalidad'}, 
                                                    columns = ['modalidad_ingreso.codigo','modalidad_ingreso.nombre'] )

    if form.accepts(request.vars, session):
        response.flah = 'Datos cargados'

    return dict(form=form, carrera=carrera, modalidad_ingreso=modalidad_ingreso)





