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

    return dict(facebook=facebook)

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

    dato_admin = db(db.auth_user.username=='root').select()
    
    if len(dato_admin)==0:
    
        # limpia las tablas de control de acceso basado en roles
        db(db.auth_user).delete()
        db(db.auth_group).delete()
        db(db.auth_membership).delete()
        db(db.auth_permission).delete()
        db(db.auth_event).delete()
        db(db.pais).delete()
        db(db.estado).delete()
        db(db.carrera).delete()
        db(db.modalidad_ingreso).delete()

        #-----------
        # crea todos los grupos de usuarios base
        auth.add_group('root')
        auth.add_group('tecnico_control_estudio')
        auth.add_group('director_control_estudio')
        auth.add_group('director_escuela')

        auth.add_group('personal_control_estudio')
        auth.add_group('estudiante')
        auth.add_group('profesor')
        auth.add_group('coordinador_asignatura')
        auth.add_group('sin_asignar')
        #-----------
        
        #registra al administrador
        my_crypt = CRYPT(key=auth.settings.hmac_key)
        id_user = db.auth_user.insert(username='root', first_name='Root', password=my_crypt('root')[0])
        db.acceso.insert(user=id_user, status='a')
        #-----------


        #agrega al administrador al grupo root
        auth.add_membership('root', id_user)
        db(db.auth_membership.user_id!=id_user).delete()
        #-----------

        # agerga un pais y un estado
        db.pais.insert(nombre='Venezuela')
        db.estado.insert(nombre='Fuera de Venezuela')
        db.estado.insert(nombre='Carabobo')

        # agrega una carrera
        db.carrera.insert(codigo=613, nombre='Odontología')

        # agrega modalidad_ingreso
        db.modalidad_ingreso.insert(codigo='1', nombre='Convenio')
        db.modalidad_ingreso.insert(codigo='2', nombre='CNU')
        db.modalidad_ingreso.insert(codigo='3', nombre='PAI')
        db.modalidad_ingreso.insert(codigo='4', nombre='Merito Academico')
        db.modalidad_ingreso.insert(codigo='5', nombre='Equivalencia')
        db.modalidad_ingreso.insert(codigo='6', nombre='Traslado')
        db.modalidad_ingreso.insert(codigo='7', nombre='Merito Deportivo')
        db.modalidad_ingreso.insert(codigo='8', nombre='Por Oficio')
        db.modalidad_ingreso.insert(codigo='A', nombre='Merito Cultural')
        db.modalidad_ingreso.insert(codigo='B', nombre='Merito Cientifico')
        db.modalidad_ingreso.insert(codigo='C', nombre='Curso Introductorio')
        db.modalidad_ingreso.insert(codigo='D', nombre='Discapacidad Fisica')
        db.modalidad_ingreso.insert(codigo='E', nombre='Cambio de Escuela')
        db.modalidad_ingreso.insert(codigo='M', nombre='Cola Merito ACAD')
        db.modalidad_ingreso.insert(codigo='N', nombre='CNU COLA')
        db.modalidad_ingreso.insert(codigo='P', nombre='PAI Corrida')
        db.modalidad_ingreso.insert(codigo='R', nombre='Reincorporación')
        db.modalidad_ingreso.insert(codigo='S', nombre='2da Carrera')
        db.modalidad_ingreso.insert(codigo='Z', nombre='Programa Elejo Zuloaga')
        db.modalidad_ingreso.insert(codigo='I', nombre='Población Indigena')




        response.flash = 'Configuracion de admin realizada'
    else:
        response.flash = 'ya existe configuracion de admin'

    return dict()


























