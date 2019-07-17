#from domain import Todo
from .todo_repository import TodoRepository


class TodoIntractor:

    def __init__(self, repository):
        self.todo_repository: TodoRepository = repository
        pass

    def add_todo(self, todo):
        self.todo_repository.add_todo(todo)
    
    def get_todo(self, _id):
        return self.todo_repository.get_todo(_id)

    def get_todos(self):
        return self.todo_repository.get_todos()

    def delete_todo(self, _id):
        return self.todo_repository.delete_todo(_id)

