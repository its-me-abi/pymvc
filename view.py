
class view:
    "extend this code "
    def __init__(self):
        pass

class example (view):
    "this is example usage of view "
    def ask_question(self,text):
        return input(text)
    
    def show_text(self,text):
        print (text)
