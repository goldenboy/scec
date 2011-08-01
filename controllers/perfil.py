# -*- coding: utf-8 -*-

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
