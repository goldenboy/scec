# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """

    facebook = '<script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script>'
    facebook +='<fb:activity site="http://www.facebook.com/#!/fundaodontologia" width="890"'
    facebook +='height="500" header="false" font="arial" border_color="" recommendations="false"></fb:activity>'

    facebook = None



    return dict(facebook=XML(facebook))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    if request.args:
        if request.args[0]=='profile':
            redirect (URL('perfil','index'))
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id[
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs bust be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())



def setup():

    dato_admin = db(db.auth_group.role=='root').select()
    
    if len(dato_admin)==0:
    
        # limpia las tablas de control de acceso basado en roles
        db(db.auth_user.id>0).delete()
        db(db.auth_group.id>0).delete()
        db(db.auth_membership.id>0).delete()
        db(db.auth_permission.id>0).delete()
        db(db.auth_event.id>0).delete()
        #-----------

        # crea todos los grupos de usuarios base
        auth.add_group('estudiante')
        auth.add_group('profesor')
        auth.add_group('control_estudio')
        auth.add_group('autoridad')
        auth.add_group('root')
        #-----------
        
        #registra al administrador
        my_crypt = CRYPT(key=auth.settings.hmac_key)
        id_user = db.auth_user.insert(username='root', password=my_crypt('root')[0])
        #-----------


        #agrega al administrador al grupo root
        auth.add_membership('root', id_user)
        db(db.auth_membership.user_id!=id_user).delete()
        #-----------


        response.flash = 'Configuracion de admin realizada'
    else:
        response.flash = 'ya existe configuracion de admin'

    return dict()
























