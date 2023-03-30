from functools import wraps

from flask import Markup, flash, url_for, redirect
from flask_login import current_user

#  过滤未确认用户
# 使用functools模块提供的wraps装饰器可以避免被装饰函数的特殊属性被更 改，比如函数名称__name__被更改。
def confirm_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            message = Markup(
                'Please confirm your account first.'
                'Not receive the email?'
                '<a class="alert-link" href="%s">Resend Confirm Email</a>' %
                url_for('auth.resend_confirm_email'))
            flash(message, 'warning')
            return redirect(url_for('main.index'))
        return func(*args, **kwargs)
    return decorated_function