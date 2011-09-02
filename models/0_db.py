# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('google:datastore')              # connect to Google BigTable
                                              # optional DAL('gae://namespace')
    session.connect(request, response, db = db) # and store sessions and tickets there
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
else:                                         # else use a normal relational database
    db = DAL('sqlite://storage.sqlite')       # if not, use SQLite or other DB

# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Mail, Auth, Crud, Service, PluginManager, prettydate
mail = Mail()                                  # mailer
auth = Auth(db)                                # authentication/authorization
crud = Crud(db)                                # for CRUD helpers using auth
service = Service()                            # for json, xml, jsonrpc, xmlrpc, amfrpc
plugins = PluginManager()                      # for configuring plugins

#mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
mail.settings.server = 'smtp.gmail.com:587'  # your SMTP server
mail.settings.sender = 'diazluis2007@gmail.com'         # your email
mail.settings.login = 'diazluis2007:luis3429dm7'      # your credentials or None

auth.settings.hmac_key = '<your secret key>'   # before define_tables()
auth.define_tables(username=True)                           # creates all needed tables
auth.settings.mailer = mail                    # for user email verification
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['verify_email'])+'/%(key)s to verify your email'
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['reset_password'])+'/%(key)s to reset your password'

#########################################################################
## If you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, uncomment and customize following
# from gluon.contrib.login_methods.rpx_account import RPXAccount
# auth.settings.actions_disabled = \
#    ['register','change_password','request_reset_password']
# auth.settings.login_form = RPXAccount(request, api_key='...',domain='...',
#    url = "http://localhost:8000/%s/default/user/login" % request.application)
## other login methods are in gluon/contrib/login_methods
#########################################################################

crud.settings.auth = None        # =auth to enforce authorization on crud

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

auth.settings.actions_disabled = ['register','retrieve_username','request_reset_password']
auth.settings.create_user_groups = False
auth.settings.registration_requires_approval = True

auth.messages.registration_pending = 'Cuenta sin Activar'
auth.messages.logged_in = 'Bienvenido'

id_user = (auth.user and auth.user.id) or None


db.auth_user.first_name.readable=False
db.auth_user.first_name.writable=False
db.auth_user.last_name.readable=False
db.auth_user.last_name.writable=False

db.auth_user.username.label='CI/Pasaporte'
db.auth_user.username.requires = [
    IS_INT_IN_RANGE(999999, 99999999),
    IS_NOT_IN_DB(db, 'auth_user.username')
]

db.auth_user.format = '%(username)s'





"""
    Grupos del sistema
    ##################
    root > creado por el sistema
    tecnico_control_estudio > cargado y asignado por root
    director_control_estudio > asignado por root (root activa o bloquea)
    director_escuela > asignado por root ademas de activa o bloquea

    personal_control_estudio > asignado por director control de estudios ademas de activa o bloquear 
    estudiante > asignado por director_control_estudio, (tecnico activa o bloquea)
    profesor > asignado por director_control_estudio (tecnico activa o bloquea)
    coordinador_asignatura > asignado por director_control_estudio (tecnico activa o bloquea)
    sin asignar > todo usuario cuando es cargado en el sistema
"""

_usuario_grupo = {
    '1':'root', #creado por el sistema 
    '2':'tecnico_control_estudio', # cargado y asignado por root
    '3':'director_control_estudio', # asignado por root (root activa o bloquea)
    '4':'director_escuela', # asignado por root ademas de activa o bloquea

    '5':'personal_control_estudio', # asignado por director control de estudios ademas de activa o bloquear 
    '6':'estudiante', # asignado por director_control_estudio, (tecnico activa o bloquea)
    '7':'profesor', # asignado por director_control_estudio (tecnico activa o bloquea)
    '8':'coordinador_asignatura', # asignado por director_control_estudio (tecnico activa o bloquea)
    '99':'sin_asignar'
}

def generar_codigo_seguridad(longitud=8):
    from gluon.utils import web2py_uuid
    codigo = web2py_uuid()
    return codigo[:int(longitud)]


def es_integrante_grupo(user, lista_grupo):

    grupo_rows = db(db.auth_membership.user_id==user).select()

    pertenece = False
    for grupo in grupo_rows:
        if grupo.group_id.role in lista_grupo:
            pertenece = True
            break
        
    return pertenece



_requires_nombre_apellido = [
    IS_LENGTH(minsize=3),
    IS_NOT_EMPTY()
]















