import responder
from interfaces.controllers.todo_handler import TodoHandler
from infrastructure.sql_handler import SqlHandler


def init():
    api = responder.API()

    handler = TodoHandler(SqlHandler())

    api.add_route("/todo", handler.todo_list)
    api.add_route("/todo/new", handler.new_todo)
    api.add_route("/todo/{todo_id}", handler.todo_info)
    api.add_route("/todo/{todo_id}/delete", handler.delete_todo)

    api.run()
