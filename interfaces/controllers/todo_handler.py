from interfaces.databases import sql_handler
from usecase.todo_interactor import TodoIntractor


def generate_id(SIZE=8):
    _id = ""
    for i in range(SIZE):
        _id += random.choice(string.ascii_letters)
    return _id


class TodoHandler:

    def __init__(self, sql_handler):
        self.interactor = TodoIntractor(sql_handler)


    def todo_list(self, req, resp):
        res = dict()
        for row in self.interactor.get_todos():
            res[row[0]] = {
                "todo_name": row[1],
                "description": row[2],
                "create_date": str(row[3]),
            }
        resp.media = res 

    def todo_info(self, req, resp, *, todo_id):
        res = dict()
        row = self.interactor.get_todo(todo_id)
        res[todo_id] = {
            "todo_name": row[1],
            "description": row[2],
            "create_date": row[3],
        }
        resp.media = res

    async def new_todo(self, req, resp):
        _id = generate_id()
        data = await req.media()
        todo = (
            _id,
            data.get("todo_name", ""),
            data.get("description", ""),
        )
        self.interactor.add_todo(todo)
        resp.status_code = api.status_codes.HTTP_201
        resp.text = f"http://localhost:5042/todo/{_id}"

    def delete_todo(self, req, resp, *, todo_id):
        self.interactor.delete_todo(todo_id)
        resp.status_code = api.status_codes.HTTP_204
