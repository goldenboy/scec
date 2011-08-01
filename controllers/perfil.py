# -*- coding: utf-8 -*-

def index():

    perfil = db(db.perfil.user == id_user).select()

    if len(perfil)>0:
        perfil = perfil[0]
    else:
        perfil_id = db.perfil.insert(user=id_user)
        redirect (URL('update'))

    return dict(perfil=perfil)



def update():

    perfil = db(db.perfil.user==id_user).select()[0]
    form = crud.update(db.perfil, perfil.id, deletable=False, next=URL('index'))


    return dict(form = form)





