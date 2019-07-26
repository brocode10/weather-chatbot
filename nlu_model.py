from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
def train_nlu():
    training_data = load_data('data/data.json')
    trainer = Trainer(config.load("config_spacy.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('./models/nlu', fixed_model_name = 'weathernlu')  # Returns the directory the model is stored in

if __name__ == '__main__':
    train_nlu()
    #run_nlu()
