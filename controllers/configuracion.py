# -*- coding: utf-8 -*-

def index():


    return dict()



def usuario_index():

    perfil_rows = db(db.perfil.usuario_tipo.contains(('c'))).select()
    return dict(perfil_rows=perfil_rows)





