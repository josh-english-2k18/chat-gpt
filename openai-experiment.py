#
# openai-experiment.py
#
# Written by Josh English.
#

# packages

import openai

# setup openai env

openai.api_key = '[OPENAI API KEY]'

# experiment with chat-gpt model

#model = 'text-davinci-002' # GPT-2, max-tokens: 4k
model = 'text-davinci-003' # GPT-3, max-tokens: 4k
#model = 'text-curie-001' # faster & lower-cost than davinci, max-tokens: 2k
#model = 'text-babbage-001' # very fast, lower-cost than curie, max-tokens: 2k
#model = 'text-ada-001' # fastest, lowest-cost, max-tokens: 2k

print("Using model  : " + model)

#prompt = 'Hello, how are you today?'
prompt = 'Describe an algorithm to calculate the digits of PI.'

print("Using prompt : " + prompt)

completion = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7)

#for choice in completion.choices:
#    print("  + choice   : " + choice.text)

message = completion.choices[0].text

print("Response     : " + message)

