from flask import render_template
from .db_op import lazy_con
from .sqlbld import Select
from .app import app

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


__all__ = []
