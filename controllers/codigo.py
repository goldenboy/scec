# -*- coding: utf-8 -*-



def index():

    form = SQLFORM.factory(
        Field('di', 'integer', label='CI o Pasaporte'),
        Field('codigo_seguridad', 'string', length=12),
        Field('clave', 'string', length=32, label='Clave Nueva', widget=SQLFORM.widgets.password.widget, requires= IS_LENGTH(minsize=8)),
        Field('clave_2', 'string', length=32, label='Confirmar clave', requires=IS_EQUAL_TO(request.vars.clave_2), widget=SQLFORM.widgets.password.widget),
    )

    if form.accepts(request.vars, session):

        _encontrado = db(db.auth_user.username==request.vars.di) \
                        (db.acceso.codigo_seguridad==request.vars.codigo_seguridad) \
                        (db.auth_user.id==db.acceso.user) \
                        (db.acceso.status=='c').select().first()

        if _encontrado:
            my_crypt = CRYPT(key=auth.settings.hmac_key)
            db(db.auth_user.id == _encontrado.auth_user.id).update(registration_key='', password=my_crypt(request.vars.clave)[0])
            db(db.acceso.user == _encontrado.auth_user.id).update(status='a', codigo_seguridad='')
            session.flash = 'Cuenta Activada, Contraseña Actualizada'
            form=auth()
        else:
            response.flash = 'Error sus datos no coinciden'    

    return dict(form=form)


    
















