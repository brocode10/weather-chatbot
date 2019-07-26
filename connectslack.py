from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.facebook import FacebookInput
from rasa_slack_connector import SlackInput



nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-301554437685-301730892917-382573241303-d7002d60b2678c3df8e1f78691efd86a', #app verification token
							'xoxb-301554437685-380827900208-vCh5rSsMUot25z1cAwYEpU1B', # bot verification token
							'n5rH3ztR8gTCNHdxj1mSMmaQ', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
