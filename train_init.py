from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core import training


import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	#path of training file
	training_data_file = './data/stories.md'
	#location of saving this file
	model_path = './models/dialogue'
	#keras policy uses LSTM.We can make our own model
	agent = Agent('weather_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])

	agent.train(
			training_data_file,
			#no of fake stories
			augmentation_factor = 50,
			#no of states model should remember
			#max_history = 2,
			epochs = 500,
			#no of samples per epoch
			batch_size = 10,
			#percentage of data used to validate model
			validation_split = 0.2)

	agent.persist(model_path)
