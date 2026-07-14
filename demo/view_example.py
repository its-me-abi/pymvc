from pymvc import view

class example_view (view.view):
    "this is example usage of view "
  
    def ask_question(self,text):
        return input(text)
    
    def show_text(self,text):
        print (text)
