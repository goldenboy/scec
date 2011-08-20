# -*- coding: utf-8 -*-



@auth.requires( auth.has_membership('root') or auth.has_membership('control_estudio'))
def index():

    if auth.has_membership('root'):
        perfil_rows = db(db.perfil.tipo.contains('c') ).select()

    if auth.has_membership('control_estudio'):
        perfil_rows = db(db.perfil.tipo.contains('p') | db.perfil.tipo.contains('a')).select()

    return dict(perfil_rows=perfil_rows)






@auth.requires( auth.has_membership('root') or auth.has_membership('control_estudio'))
def add():

    error = ['Error los siguiente usuarios ya estan registrados']
    if auth.has_membership('root'):
        role = 'control_estudio'
        tipo = 'c'

    elif auth.has_membership('control_estudio'):
        role = 'profesor'
        tipo = 'p'


    form = SQLFORM.factory(
        Field('di', 'integer', label='CI/Pasaporte'),
        Field('nombre', 'string', length=64),
        Field('email', 'string', length=128),
        Field('lote', 'text', length=2048),

    )

    if form.accepts(request.vars, session):
        
        #my_crypt = CRYPT(key=auth.settings.hmac_key)

        if request.vars.lote:
            dato_usuario_rows = request.vars.lote.split('\n')

            for dato_usuario in dato_usuario_rows:
                usuario_valor = dato_usuario.split('|')
                usuario_valor_di = usuario_valor[0]
                usuario_valor_nombre = usuario_valor[1]
                usuario_valor_email = usuario_valor[2]
                encontrado = db((db.auth_user.username==usuario_valor_di) | (db.auth_user.email==usuario_valor_email) ).select().first()

                if encontrado:
                    mensaje_error = 'DI: %s  Nombre: %s' % (usuario_valor_di, usuario_valor_nombre)
                    error.append(mensaje_error)
                else:
                    usuario_id = db.auth_user.insert(username=usuario_valor_di, email=usuario_valor_email, first_name=usuario_valor_nombre, registration_key='pending')
                    db.perfil.insert(di=usuario_valor_di, user=usuario_id, tipo=tipo)
                    auth.add_membership(role, usuario_id)
        else:
            usuario_valor_di = request.vars.di
            usuario_valor_nombre = request.vars.nombre
            usuario_valor_email = request.vars.email
            encontrado = db((db.auth_user.username==usuario_valor_di) | (db.auth_user.email==usuario_valor_email) ).select().first()
            if encontrado:
                mensaje_error = 'DI: %s  Nombre: %s' % (usuario_valor_di, usuario_valor_nombre)
                error.append(mensaje_error)
            else:
                usuario_id = db.auth_user.insert(username=usuario_valor_di, email=usuario_valor_email, first_name=usuario_valor_nombre, registration_key='pending')
                db.perfil.insert(di=usuario_valor_di, user=usuario_id, tipo=tipo)
                auth.add_membership(role, usuario_id)


    if len(error)>1:
        response.flash = error
    return dict(form=form)




















