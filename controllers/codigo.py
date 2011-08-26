# -*- coding: utf-8 -*-



def index():

    form = SQLFORM.factory(
        Field('di', 'integer', label='CI o Pasaporte'),
        Field('codigo_seguridad', 'string', length=12),
        Field('clave', 'string', length=32, label='Clave Nueva', widget=SQLFORM.widgets.password.widget),
        Field('clave_2', 'string', length=32, label='Confirmar clave', requires=IS_EQUAL_TO(request.vars.clave_2), widget=SQLFORM.widgets.password.widget),
    )

    if form.accepts(request.vars, session):

        _encontrado = db(db.perfil.di==request.vars.di)(db.perfil.codigo_seguridad==request.vars.codigo_seguridad)(db.perfil.status=='c').select().first()

        if _encontrado:
            my_crypt = CRYPT(key=auth.settings.hmac_key)
            db(db.auth_user.id == _encontrado.user).update(registration_key='', password=my_crypt(request.vars.clave)[0])
            session.flash = 'Contraseña Actualizada'
            form=auth()
        else:
            response.flash = 'Error sus datos no coinciden'    

    return dict(form=form)




















