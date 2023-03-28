# openai
This will introduce two types of ChatGPT: ChatGPT-3 and EdgeGPT with ChatGPT-4.

trans.py with ChatGPT-3 is an example of translation from English to French and Japanese.
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
The temperature is a determinant from 0.0 to 1.0 to control the randomness. The larger the temperature, the greater the randomness.

# EdgeGPT
EdgeGPT takes advantage of the new version of Bing (Microsoft search engine)
with ChatGPT-4.

1. $ pip install EdgeGPT

2. Install the latest Edge browser.

3. Open https://bing.com/chat

4. Install cookie-editor for Firefox or Chrome.

5. Access bing.com with Firefox or Chrome.

6. From Extensions, click cookie-Editor
<img src='fig1.png' height=500 width=400>

7. Click Export icon of cookie-editor
<img src='fig2.png' height=500 width=500>



