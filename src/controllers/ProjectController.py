from .BaseController import BaseController
import os


class ProjectController(BaseController):
    def __init__(
        self,
    ):  # This defines the constructor for ProjectController. It's the method that's called when an object of this class is created.
        super().__init__()  # This calls the __init__ method of the parent class (BaseController).

    def get_project_path(self, project_id: str):
        project_dir = os.path.join(self.files_dir, project_id)

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir
