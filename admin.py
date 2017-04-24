from flask import url_for
from flask_security import UserMixin, RoleMixin, login_required, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_admin import helpers as admin_helpers
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

#        if current_user.has_role('manager'):
#            return True

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

