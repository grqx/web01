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


__all__ = []
