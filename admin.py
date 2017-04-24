from flask import url_for
from flask_security import UserMixin, RoleMixin, login_required, \
    current_user, utils
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_admin import helpers as admin_helpers
from wtforms.fields import PasswordField
from finapp import app, db
from security import security
from models import Manager, ApprovalList, Role, Client


#  Add Admin 
admin = Admin(
            app, 'Management', base_template='my_master.html', 
            template_mode='bootstrap3')


class SuperAdminModelView(ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))
    
    #  Don't display the password on the list of Users
    column_exclude_list = list = ('password',)

    #  Don't include the standard password field when creating or editing a User (but see below)
    form_excluded_columns = ('password',)

    #  Automatically display human-readable names for the current 
    #  and available Roles when creating or editing a User
    column_auto_select_related = True
    
    #  Masked password field
    def scaffold_form(self):

        # Start with the standard form as provided by Flask-Admin
        form_class = super(SuperAdminModelView, self).scaffold_form()

        # Add a password field, naming it "password2" and labeling it "New Password".
        form_class.password2 = PasswordField('New Password')
        return form_class
    
    def on_model_change(self, form, model, is_created):

        # If the password field isn't blank...
        if len(model.password2):

            # ... then encrypt the new password.
            model.password = utils.encrypt_password(model.password2)


class AdminModelView(SuperAdminModelView):

    def is_accessible(self):

        if current_user.has_role('manager'):
            return True

        return super(AdminModelView, self).is_accessible()


admin.add_view(SuperAdminModelView(Manager, db.session))
admin.add_view(AdminModelView(ApprovalList, db.session))
admin.add_view(AdminModelView(Client, db.session))


@security.context_processor
def security_context_processor():
    return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
            get_url=url_for
            )

