from . import model_example
from . import view_example
from . import controller_example

from pymvc import mvc

class example_main( mvc.mvc ):
  
    ""
    "entrypoint of this software .it is written in mvc design pattern"
    "extend this class and create your own implementation "
  
    def __init__(self):
        self.view = view_example.example_view()
        self.model = model_example.example_model()
        self.controller = controller_example.example_controller(self.view, self.model)

    def run(self):
        self.controller.run()
