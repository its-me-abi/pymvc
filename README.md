# pymvc
mvc design pattern framework with eample in python. you can extend it and use

### what is mvc design pattern
```
   it a highlevel structure of writing code .it is a way  to create a professional or 
   easly maintainable and easy to understand code 
   we should seperate code into 3 things.called model view and controller.
   
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
