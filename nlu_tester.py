from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.model import Trainer
from rasa_nlu.components import ComponentBuilder
import logging

logger = logging.getLogger(__name__)
#logging.basicConfig(level="DEBUG")


builder = ComponentBuilder(use_cache=True)

model_directory ="./models/nlu/default/weathernlu"

interpreter = Interpreter.load(model_directory, builder)
interpreter_clone = Interpreter.load(model_directory, builder)


def sent_parse():
    sent=input('''please enter the sentence: or press 'E' to exit \n\n''')
    if(sent=='E'):
        return
    else:
        print(interpreter_clone.parse(sent))
        sent_parse()

if __name__ == '__main__':
 
    #logging.basicConfig(filename=config['log_file'], level=config['log_level'])
    sent_parse()        
    

