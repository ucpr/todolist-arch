import os
import psycopg2


class SqlHandler:
    _dsn = "postgresql://todo:todo@localhost:5432/todo"

    def __init__(self):
        self.con = psycopg2.connect(self._dsn)
