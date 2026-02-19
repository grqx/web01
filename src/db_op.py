import os.path
import threading
import sqlite3

DB_FNAME = 'app.db'
DB_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, DB_FNAME))

_lcl = threading.local()

def lazy_con() -> sqlite3.Connection:
    global _lcl
    try:
        return getattr(_lcl, 'con')
    except AttributeError:
        newcon = sqlite3.connect(DB_PATH)
        setattr(_lcl, 'con', newcon)
        return newcon

def shutdown_con():
    global _lcl
    try:
        con = getattr(_lcl, 'con')
        con.close()
        setattr(_lcl, 'con', None)
    except AttributeError:
        ...
