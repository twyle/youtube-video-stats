from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register_client():
    """Register a new client."""
    return 'Client registered.'


@auth.route('/confirm_email', methods=['GET'])
def confirm_client_email():
    """Confirm email address."""
    return 'Email confirmed.'


@auth.route('/login_client', methods=['POST'])
def login_client():
    """Login a registered, confirmed client."""
    return 'Logged in.'


@auth.route('/request_password_reset', methods=['GET'])
def request_client_password_rest():
    """Request a client password reset."""
    return 'Password reset.'


@auth.route('/reset_password', methods=['POST'])
def reset_client_password():
    """Reset a client password."""
    return 'Password reset.'


@auth.route('/refresh_token', methods=['POST'])
def refresh_token():
    """Refresh an expired token."""
    return 'Token refreshed.'
