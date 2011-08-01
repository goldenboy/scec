# -*- coding: utf-8 -*-

def index():

    
    perfil = db(db.perfil.user == id_user).select()
    presentacion_perfil = 'vista'

    socio_e = db(db.socio_e.user == id_user).select()
    presentacion_socio_e = 'vista'

    if len(perfil)>0:
        perfil = perfil[0]
    else:
        perfil_id = db.perfil.insert(user=id_user)
        perfil = crud.update(db.perfil, perfil_id)
        presentacion_perfil = 'form'

    if len(socio_e)>0:
        socio_e = socio_e[0]
    else:
        socio_id = db.socio_e.insert(user=id_user)
        socio_e = crud.update(db.socio_e, socio_id)
        presentacion_socio_e = 'form'

    return dict(perfil=perfil, presentacion_perfil=presentacion_perfil, 
                socio_e=socio_e, presentacion_socio_e=presentacion_socio_e)



def update():

    perfil = None
    socio_e = None

    if request.args:
        if request.args[0]=='perfil':
            perfil = db(db.perfil.user==id_user).select()[0]
            perfil = crud.update(db.perfil, perfil.id, deletable=False, next=URL('index'))


        if request.args[0]=='socio_e':
            socio_e = db(db.socio_e.user==id_user).select()[0]
            socio_e = crud.update(db.socio_e, socio_e.id, deletable=False, next=URL('index'))

    return dict(perfil = perfil, socio_e=socio_e)





