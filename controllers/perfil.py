# -*- coding: utf-8 -*-

def index():


    perfil = db(db.perfil.user == id_user).select()
    socio_e = db(db.socio_e.user == id_user).select()

    if len(perfil)>0:
        perfil = perfil
    else:
        perfil_id = db.perfil.insert(user=id_user)
        perfil = crud.update(db.perfil, perfil_id)

    if len(socio_e)>0:
        socio_e = socio_e
    else:
        socio_id = db.socio_e.insert(user=id_user)
        socio_e = crud.update(db.socio_e, socio_id)


    return dict(perfil=perfil, socio_e=socio_e)



def update():

    perfil = db(db.perfil.user==id_user).select()

    if len(perfil)==0:
        perfil_id = db.perfil.insert(user=id_user)
    else:
        perfil_id = perfil[0].id

    form_perfil = crud.update(db.perfil, perfil_id, deletable=False, next=URL('index'))
    field_auth = db.auth_user
    field_auth.email.writable = False
    form = crud.update(field_auth, id_user)

    return dict(form=auth(), form_perfil=form_perfil)
