# -*- coding: utf-8 -*-



@auth.requires_membership('root')
def index():

    _usuario_tipo = request.vars.tipo

    """ lista los siguiente usuarios:
       * tecnico de control_estudio [2]
       * Director de Control de Estudio [3]
       * Director de Escuela [4]
       * Personal de control de estudios
    """
    query_perfil = db(db.perfil.user==db.acceso.user).select()
    perfil_rows = query_perfil.find(lambda row: es_integrante_grupo(row.perfil.user,['tecnico_control_estudio','director_control_estudio','director_escuela','personal_control_estudio','sin_asignar']))

    return dict(perfil_rows=perfil_rows)






@auth.requires_membership('root')
def add():

    mensaje_error = None

    _tipo = {
        '2':'Tecnico de Control de Estudio',
        '3':'Director de Control de Estudio',
        '4':'Director de Escuela',
        '5':'Personal de Control de Estudios',
        '99': 'Sin asignar'
     }


    form = SQLFORM.factory(
        Field('di', 'integer', label='CI/Pasaporte'),
        Field('nombre1', 'string', length=64, label='Primer Nombre'),
        Field('apellido1', 'string', length=64, label='Primer Apellido'),
        Field('nombre2', 'string', length=64, label='Segundo Nombre'),
        Field('apellido2', 'string', length=64, label='Segundo Apellido'),
        Field('email', 'string', length=128),
        Field('tipo', 'integer', requires=IS_IN_SET(_tipo, zero=None))
    )

    if form.accepts(request.vars, session):
        
        #my_crypt = CRYPT(key=auth.settings.hmac_key)

        _usuario_di = request.vars.di
        _usuario_nombre1 = request.vars.nombre1
        _usuario_apellido1 = request.vars.apellido1
        _usuario_nombre2 = request.vars.nombre2
        _usuario_apellido2 = request.vars.apellido2
        _usuario_email = request.vars.email
        _usuario_tipo = request.vars.tipo
        _encontrado = db((db.auth_user.username==_usuario_di) | (db.auth_user.email==_usuario_email) ).select().first()
        if _encontrado:
            mensaje_error = 'DI: %s  Nombre: %s ya existe' % (_usuario_di, _usuario_nombre1)
            
        else:
            _usuario_id = db.auth_user.insert(username=_usuario_di, email=_usuario_email, first_name=_usuario_di, registration_key='pending')
            auth.add_membership(user_id=_usuario_id, role=_usuario_grupo[_usuario_tipo])
            db.perfil.insert(user=_usuario_id, di=_usuario_di, nombre1=_usuario_nombre1, apellido1=_usuario_apellido1, nombre2=_usuario_nombre2, apellido2=_usuario_apellido2 )
            db.acceso.insert(user=_usuario_id)
            session.flash = 'Usuario Agregado'
            redirect (URL('index'))


    if mensaje_error:
        response.flash = mensaje_error

    return dict(form=form)



@auth.requires_membership('root')
def status():

    response.view = 'usuario/add.html'
    form = None
    _usuario_id = request.args[0]


    _acceso = db(db.acceso.user==_usuario_id).select().first()


    if _acceso:
        if auth.has_membership('root') and es_integrante_grupo(_acceso.user, ['tecnico_control_estudio','personal_control_estudio','director_control_estudio','director_escuela']):
            form = SQLFORM.factory(
                        Field('username', 'integer', default=_acceso.user.username, writable=False),
                        Field('status', 'string', length=1, requires=IS_IN_SET({'b':'Bloqueado','c':'Codigo Nuevo'}, zero=None)),
                        Field('user', default=_acceso.user, writable=False, readable=False),
            )
            if form.accepts(request.vars, session):

                if request.vars.status == 'b':
                    db(db.acceso.user==_acceso.user).update(status='b',codigo_seguridad='')
                    db(db.auth_user.id==_acceso.user).update(registration_key='pending')
                elif request.vars.status == 'c':
                    _codigo_seguridad = generar_codigo_seguridad()
                    db(db.acceso.user==_acceso.user).update(status='c', codigo_seguridad=_codigo_seguridad)
                    db(db.auth_user.id==_acceso.user).update(registration_key='pending')

                session.flash = 'Status Actualizado'
                redirect(URL('index'))

              
    return dict(form=form)



@auth.requires_membership('root')
def update_grupo():

    response.view = 'usuario/add.html'
    form = None
    _usuario_id = request.args[0]

    _grupo = ['tecnico_control_estudio','director_control_estudio','director_escuela','personal_control_estudio']

    _usuario_grupo = db(db.auth_membership.user_id==_usuario_id).select()


    
    _usuario_pertenece =  [_row.group_id.role  for _row in _usuario_grupo]

    form = SQLFORM.factory(
        Field('username', 'integer', default=_usuario_grupo[0].user_id.username, writable=False),
        Field('grupo', 'list:string', default=_usuario_pertenece , requires=IS_IN_SET(_grupo, multiple=True, zero=None), widget=SQLFORM.widgets.checkboxes.widget),
        Field('user', default=_acceso.user, writable=False, readable=False),
    )

    if form.accepts(request.vars, session):
        db(db.auth_membership.user_id==_usuario_id).delete()
        if request.vars.grupo:
            if isinstance(request.vars.grupo, basestring):
                auth.add_membership(request.vars.grupo, _usuario_id)
            else:
                for nuevo in request.vars.grupo: auth.add_membership(nuevo, _usuario_id)
        else:
            auth.add_membership('sin_asignar', _usuario_id)


        session.flash = 'Grupo actualizado'
        redirect (URL('index'))
    return dict(form=form)





















