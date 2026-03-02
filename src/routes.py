import bcrypt

from flask import redirect, render_template, request, Response, session
from uuid import uuid4
from .db_op import lazy_con
from .sqlbld import Select
from .app import app

assert app, 'app must not be none at the time of import'

ADMIN_PASSWD = b'$2b$12$umixqSvkhVhA.USi6QAokO.duMRKOGZyjwV.uzhRyfBPfbORpchLy'


def init_routes():
    app.secret_key = uuid4().bytes

@app.route('/')
def _root():
    with lazy_con() as con:
        return render_template('index.html', bikes=Select(
            r'SELECT bike_id, maker_id, model FROM Bikes').execute(
                con.cursor()).fetchall())

@app.route('/bike/<int:bike_id>')
def _bike(bike_id: int):
    with lazy_con() as con:
        return render_template('bike.html', bike=Select(
            r'SELECT * FROM Bikes').where('bike_id = ?').execute(
                con.cursor(), (bike_id, )).fetchone())

@app.route('/login', methods=['GET', 'POST'])
def _login():
    if request.method == 'POST':
        k = request.form.get('k')
        if not k:
            return Response(
                'Expected "k" in form', status=400,
            )
        if not bcrypt.checkpw(k.encode(), ADMIN_PASSWD):
            return Response(
                'Password incorrect', status=403,
            )
        session['l'] = True
        return redirect('/admin')

    if session.get('l') is True:
        return redirect('/admin')
    return render_template('login.html')

@app.route('/admin')
def _admin():
    return 'Hello, admin!'


__all__ = []
