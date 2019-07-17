#from domain import Todo
from sql_handler import *


class TodoRepository:

    def __init__(self, handler):
        self.sql_handler = handler

    def add_todo(self, todo):
        statement = "INSERT INTO todos (id, task_name, description) VALUES (%s, %s, %s)"
        with self.sql_handler.con.cursor() as cursor:
            # TODO: todo is class. required tuple
            cursor.execute(statement, todo)
        conn.commit()

    def get_todo(self, _id):
        statement = "SELECT * FROM todos WHERE id = %s"
        with self.sql_handler.con.cursor() as cursor:
            cursor.execute(statement, (_id,))
            return cursor.fetchone()

    def get_todos(self):
        statement = "SELECT * FROM todos"
        with self.sql_handler.con.cursor() as cursor:
            cursor.execute(statement)
            for row in cursor:
                yield row


    def delete_todo(self, _id):
        statement = "DELETE FROM todos WHERE id = %s"
        with self.sql_handler.con.cursor() as cursor:
            cursor.execute(statement, (_id,))
        conn.commit()

