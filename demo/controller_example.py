from pymvc import view
from pymvc import model

class example_controller (controller.controller) :
    
    "this is an example usage for contoller"
    
    def run(self):
        
        try:
            text = self.view.ask_question("enter some text it will be saved to file")
            self.model.save_to_file(text)
            self.view.show_text("successfully writen to file")
            
        except Exception as error:
            self.view.show_text("an error occuered while saving to file")
