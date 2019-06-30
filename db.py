import os
from typing import Tuple
import psycopg2


def get_connection():
    dsn = "postgresql://todo:todo@localhost:5432/todo"
    return psycopg2.connect(dsn)


def create_todo(conn, values):
    statement = "INSERT INTO todos (id, task_name, description) VALUES (%s, %s, %s)"
    with conn.cursor() as cursor:
        cursor.execute(statement, values)
    conn.commit()


def get_todos(conn):
    statement = "SELECT * FROM todos"
    with conn.cursor() as cursor:
        cursor.execute(statement)
        for row in cursor:
            yield row


def get_todo(conn, _id) -> Tuple:
    statement = "SELECT * FROM todos WHERE id = %s"
    with conn.cursor() as cursor:
        cursor.execute(statement, (_id,))
        return cursor.fetchone()


def delete_todo(conn, _id):
    statement = "DELETE FROM todos WHERE id = %s"
    with conn.cursor() as cursor:
        cursor.execute(statement, (_id,))
    conn.commit()

