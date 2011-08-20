# -*- coding: utf-8 -*-



@auth.requires(auth.has_membership('root'))
def index():

    perfil_rows = db(db.perfil.tipo.contains('a') ).select()
    return dict(perfil_rows=perfil_rows)




@auth.requires( auth.has_membership('root'))
def add():

    error = ['Error los siguiente usuarios ya estan registrados']
    role = 'autoridad'
    tipo = 'a'


    form = SQLFORM.factory(
        Field('di', 'integer', label='CI/Pasaporte'),
        Field('nombre', 'string', length=64),
        Field('email', 'string', length=128),
    )

    if form.accepts(request.vars, session):
        
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




















