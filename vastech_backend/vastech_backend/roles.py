from rolepermissions.roles import AbstractUserRole

class AddUsers(AbstractUserRole):
    available_permissions = {
        'create_new_user': True,
    }

class Loans(AbstractUserRole):
    available_permissions = {
        'approve_loan_application': True,
    }