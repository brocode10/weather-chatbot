from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.facebook import FacebookInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)


input_channel = FacebookInput(
    fb_verify="12345",  # you need tell facebook this token, to confirm your URL
    fb_secret="3c352610a6ea8c4cb39c9df28d325889",  # your app secret
    fb_access_token="EAADcYdiRB8gBAHoZBQhFj9U4ZBohZB533HUCN7b5ScFHcWAQZAQC6iOw2IZCLshTNZBvPP52T3BUwvnZA8thArXiHl3JG2rhHy2x0Jk1HNWPZCfs5uw4naEWZBROQiSLfQJChRB59yeZAaaRwcv2tF5MjkwfuytWKpZAZAgZA7iXBppAk6RB7tuBbNVAB"   # token for the page you subscribed to
)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
