# chat-gpt
ChatGPT from OpenAI API Experiment

## Setup
1. You will need an account with OpenAI

Use your account to generate an API key: https://platform.openai.com/account/api-keys

2. Install python 3.7 or later

Make sure to include the `python-dev` (i.e. `python-devel`) packages so that various OpenAI dependencies will install correctly. You will also need to modern compiler such as `gcc` installed. Without these, the `aiohttp`, `frozenlist`, `multidict` and `yarl` packages used by the OpenAI API will not be installed.

3. Ensure that `pip` is up to date.
```
$ python3 -m pip install --upgrade pip
```

4. Install OpenAI
```
$ pip3 install openai
```

5. Modify `openai-experiment.py` and replace the value of `openai.api_key` with your OpenAI API key.

6. Execute the experiment:
```
$ python3 openai-experiment.py
```

## Comparing OpenAI Models
This experiment is already configured to experiment with various [models](https://platform.openai.com/docs/models/overview), which can be selected in this code section:
```
# experiment with chat-gpt model

#model = 'text-davinci-002' # GPT-2, max-tokens: 4k
model = 'text-davinci-003' # GPT-3, max-tokens: 4k
#model = 'text-curie-001' # faster & lower-cost than davinci, max-tokens: 2k
#model = 'text-babbage-001' # very fast, lower-cost than curie, max-tokens: 2k
#model = 'text-ada-001' # fastest, lowest-cost, max-tokens: 2k
```

### Ada Model Experiment
```
$ python3 openai-experiment.py
Using model  : text-ada-001
Using prompt : Describe an algorithm to calculate the digits of PI.
Response     :

The algorithm to calculate the digits of PI is as follows:

1) Add 1 and 2 together.
2)eca
3)Pi
4)Ea
```

### Davinci Model Experiment
```
$ python3 openai-experiment.py
Using model  : text-davinci-003
Using prompt : Describe an algorithm to calculate the digits of PI.
Response     :

1. Start with a variable x set to 0.
2. For each iteration, increase x by 1.
3. Calculate the value of 4/(x*(x+2)*(x+4))
4. Multiply the result from step 3 by 16^(x-1).
5. Add the result from step 4 to a running total.
6. Repeat steps 2-5 until the desired number of digits of PI has been calculated.
```
