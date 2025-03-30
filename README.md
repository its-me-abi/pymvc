# pymvc
mvc design pattern framework with eample in python.

### what is mvc design pattern
```
   It is a high-level structure for writing code. It provides a way to create professional,
   easily maintainable, and easy-to-understand code.
   We should separate the code into three components: Model, View, and Controller (MVC).

   
   it means
   
      * we must start execution from controller. 
      * controller will start graphical user interface (view functions)
      * it will also start core backend code ( model functions).
      * we should not call model functions from view and we should not call view functions from model. 
      * controller can call view and model functions. so they can communicate
   
   if you implemented this basic code then it automaticaly becomes a professional code
```

### what are these files
```
   mvc.py  
      it contain starting point .the main code.it runs controller
   
   model.py
    contain backend code or code which uses lowlevel functions
   
   view.py
      contains graphical user interface
   
   controller.py
      it contain code responsible for managing model and view.it runs view and model
```

### usage

```
from pymvc import view
from pymvc import model
from pymvc import controller


class example_mvc:
    ""
    "entrypoint of this software .it is written in mvc design pattern"
    "extend this class and create your own implementation "
    def __init__(self):
        self.view = view.example()
        self.model = model.example()
        self.controller = controller.example(self.view, self.model)

    def run(self):
        self.controller.run()

if __name__ == "__main__":
    example_mvc().run()
```
