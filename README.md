# openai
trans.py is an example of translation from English to French and Japanese.
The text message "Translate this into 1. French and 2. Japanese:\n\nWhat rooms do you have available?\n." is fed to openai to generate the response.

<pre>
1.API key:
https://platform.openai.com/account/api-keys
open account to obtain API key for OpenAI

2. $ pip install openai

3. $ cat trans.py
# -*- coding: utf-8 -*-
import openai

openai.api_key ="API-key"

res = openai.Completion.create(
  model="text-davinci-003",
  prompt="Translate this into 1. French and 2. Japanese:\n\nWhat rooms do you have available?\n.",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(res['choices'][0]['text'])

4. $ python trans.py
1. Quels salles avez-vous disponibles?
2. どの部屋が利用可能ですか？
</pre>
# Exercises
1. Write a program for asking a question and a temperature to ChatGPT and returning the response.
The temperature is a determinant to control the randomness. The larger the temperature, the greater the randomness.
