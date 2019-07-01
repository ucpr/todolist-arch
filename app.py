import random
import string
import responder

import db

api = responder.API()


def generate_id(SIZE=8):
    _id = ""
    for i in range(SIZE):
        _id += random.choice(string.ascii_letters)
    return _id


@api.route("/todo")
class Index:
    def on_get(self, req, resp):
        """
        Return
        ------
        Content-Type: application/json
    
        {
            "{id}": {
                "{task_name}": "hoge",
                "{description}": "hoge",
                "{create_date}": "DATETIME",
            },
        }
        """
        res = dict()
        with db.get_connection() as conn:
            for row in db.get_todos(conn):
                res[row[0]] = {
                    "todo_name": row[1],
                    "description": row[2],
                    "create_date": str(row[3]),
                }
        resp.media = res
    

@api.route("/todo/new")
class Create:
    async def on_post(self, req, resp):
        _id = generate_id()
        data = await req.media()
        with db.get_connection() as conn:
            new_todo = (
                _id,
                data.get("todo_name", ""),
                data.get("description", ""),
            )
            db.create_todo(conn, new_todo)
        resp.status_code = api.status_codes.HTTP_201
        resp.text = f"http://localhost:5042/todo/{_id}"


@api.route("/todo/{todo_id}/delete")
class Delete:
    def on_delete(self, req, resp, *, todo_id):
        with db.get_connection() as conn:
            db.delete_todo(conn, todo_id)
        resp.status_code = api.status_codes.HTTP_204
    

@api.route("/todo/{todo_id}")
class TodoInfo:
    def on_get(self, req, resp, *, todo_id):
        """
        Return
        ------
        {
            "{id}": {
                "{task_name}": "hoge",
                "{description}": "hoge",
                "{create_date}": "DATETIME",
            }
        }
        """
        res = dict()
        with db.get_connection() as conn:
            row = db.get_todo(conn, todo_id)
            res[todo_id] = {
                "todo_name": row[1],
                "description": row[2],
                "create_date": str(row[3]),
            }
        resp.media = res


if __name__ == "__main__":
    api.run()
