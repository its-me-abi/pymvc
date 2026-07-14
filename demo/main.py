from pymvc import view
from pymvc import model
from pymvc import controller
from pymvc import mvc

class example_main( mvc.mvc ):
  
    ""
    "entrypoint of this software .it is written in mvc design pattern"
    "extend this class and create your own implementation "
  
    def __init__(self):
        self.view = view.example()
        self.model = model.example()
        self.controller = controller.example(self.view, self.model)

    def run(self):
        self.controller.run()
