
class model:
    pass

class example (model):
    "this is an example for model "
    filename = "helo.txt"

    def save_to_file( self,text):
           file = open(self.filename,"w")
           file.write(text)
           file.close()
           

