from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.facebook import FacebookInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)


input_channel = FacebookInput(
    fb_verify="xxxx",  # you need tell facebook this token, to confirm your URL
    fb_secret="xxxx",  # your app secret
    fb_access_token="xxxx"   # token for the page you subscribed to
)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
