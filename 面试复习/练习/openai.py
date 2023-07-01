import os
import openai

api_key = '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'
openai.api_key = api_key

model = 'text-davinci-003'

response = openai.Completion.create(
  prompt='How big is the moon',
  model=model
)

print(response)