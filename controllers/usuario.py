# -*- coding: utf-8 -*-



@auth.requires( auth.has_membership('root') or auth.has_membership('tecnico_control_estudio') )
def index():

    _usuario_tipo = request.vars.tipo

    if auth.has_membership('root'):
        """ lista los siguiente usuarios:
          * tecnico de control_estudio [2]
          * Director de Control de Estudio [3]
          * Director de Escuela [4]
        """
#        perfil_rows = db(db.perfil.tipo.contains('2') | db.perfil.tipo.contains('3') |
#                         db.perfil.tipo.contains('4') )(db.perfil.tipo==_usuario_tipo).select(orderby=~db.perfil.di)

        perfil_rows = db(db.perfil.user==db.auth_membership.user_id)(db.auth_membership.group_id==auth.id_group('tecnico_control_estudio') or 
                                                                    db.auth_membership.group_id==auth.id_group('director_control_estudio') or 
                                                                    db.auth_membership.group_id==auth.id_group('director_escuela')).select()

    if auth.has_membership('tecnico_control_estudio'):
        """ lista los siguiente usuarios:
          * estudiante [6]
          * profesor  [7]
          * coordinador_asignatura [8]
        """
        perfil_rows = db(db.perfil.user==db.auth_membership.user_id)(db.auth_membership.group_id==auth.id_group('estudiante') or 
                                                                    db.auth_membership.group_id==auth.id_group('profesor') or 
                                                                    db.auth_membership.group_id==auth.id_group('coordinador_asignatura')).select()

    return dict(perfil_rows=perfil_rows)






@auth.requires( auth.has_membership('root') or auth.has_membership('tecnico_control_estudio') )
def upload():
    
    _tipo = {
        0:'Seleccionar'
    }

    error = ['Error los siguiente usuarios ya estan registrados']
    if auth.has_membership('root'):
        _tipo = {
            2:'tecnico_control_estudio',
            3:'director_control_estudio',
            4:'director_escuela'
        }

    if auth.has_membership('tecnico_control_estudio'):
        _tipo = {
            99:'Sin asignar',
        }


    form = SQLFORM.factory(
        Field('di', 'integer', label='CI/Pasaporte'),
        Field('nombre1', 'string', length=64, label='Primer Nombre'),
        Field('apellido1', 'string', length=64, label='Primer Apellido'),
        Field('nombre2', 'string', length=64, label='Segundo Nombre'),
        Field('apellido2', 'string', length=64, label='Segundo Apellido'),
        Field('email', 'string', length=128),
        Field('lote', 'text', length=2048),
        Field('tipo', 'integer', requires=IS_IN_SET(_tipo, zero=None))
    )

    if form.accepts(request.vars, session):
        
        #my_crypt = CRYPT(key=auth.settings.hmac_key)


        
        if request.vars.lote:
            _vector_usuario = request.vars.lote.split('\n')
            for _usuario in _vector_usuario:
                _usuario_di = _usuario[0]
                
            pass
        else:
            _usuario_di = request.vars.di
            _usuario_nombre = request.vars.nombre
            _usuario_email = request.vars.email
            _usuario_tipo = request.vars.tipo
            _encontrado = db((db.auth_user.username==_usuario_di) | (db.auth_user.email==_usuario_email) ).select().first()
            if _encontrado:
                mensaje_error = 'DI: %s  Nombre: %s' % (_usuario_di, _usuario_nombre)
                error.append(mensaje_error)
            else:
                _usuario_id = db.auth_user.insert(username=_usuario_di, email=_usuario_email, first_name=_usuario_nombre, registration_key='pending')
                _grupo_id = auth.add_group('user_%i' % int(_usuario_id))
                auth.add_membership(request.vars.tipo, _usuario_id)
                auth.add_membership(_grupo_id, _usuario_id)
                db.perfil.insert(di=_usuario_di, user=_usuario_id, tipo=_usuario_tipo)

                redirect (URL('index'))


    if len(error)>1:
        response.flash = error

    return dict(form=form)




def status():

    form = None
    _usuario_user = request.vars.user

    if auth.has_membership('root'):
        _encontrado = db(db.perfil.user==_usuario_user)(db.perfil.tipo.contains('2') | 
                                                        db.perfil.tipo.contains('3') |
                                                        db.perfil.tipo.contains('4')).select().first()

        if _encontrado:
            form = SQLFORM.factory(
                        Field('user', 'integer', default=_usuario_user, writable=False, readable=False),
                        Field('status', 'string', length=1, default=_encontrado.status, requires=db.perfil.status.requires)
                    )
            if form.accepts(request.vars, session):

                if request.vars.status == 'c':
                    _codigo_seguridad = generar_codigo_seguridad()
                    db(db.perfil.user==request.vars.user).update(status=request.vars.status, codigo_seguridad=_codigo_seguridad)
                    db(db.auth_user.id==request.vars.user).update(registration_key='pending')
                elif request.vars.status == 'b':
                    db(db.perfil.user==request.vars.user).update(status=request.vars.status)
                    db(db.auth_user.id==request.vars.user).update(registration_key='pending')
                else: # 'a'
                    db(db.perfil.user==request.vars.user).update(status='a')
                    db(db.auth_user.id==request.vars.user).update(registration_key='')

                session.flash = 'Status Actualizado'
                redirect(URL('index'))

              
    return dict(form=form)













