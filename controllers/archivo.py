# -*- coding: utf-8 -*-


def index():
  
    archivo_cuenta_rows = db(db.archivo_cuenta).select()

    return dict(archivo_cuenta_rows=archivo_cuenta_rows)





def upload_archivo_cuenta():

    form = crud.create(db.archivo_cuenta, next=URL('index') )

    return dict(form=form)


















