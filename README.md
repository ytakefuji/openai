# openai
Access the following site for creating your account on ChatGPT: https://chat.openai.com/

This repository will introduce two types of ChatGPT: ChatGPT-3 and EdgeGPT.

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
1. Write a program for interactively asking a question and a temperature to ChatGPT and returning the response.

The temperature is a determinant from 0.0 to 1.0 to control the randomness. The larger the temperature, the greater the randomness.

2. Write a english-to-japanese translator.

3. Write a program to collect a list of peer-reviewed papers on the specific subject.


# EdgeGPT
EdgeGPT takes advantage of the new version of Bing (Microsoft search engine)
with ChatGPT.

1. $ pip install EdgeGPT

2. Install the latest Edge browser.

3. Open https://bing.com/chat

4. Install Cookie-Editor for Edge, Firefox or Chrome.

5. Access bing.com with Edge, Firefox or Chrome.

6. From Extensions, click Cookie-Editor
<img src='fig1.png' height=400 width=300>

7. Click Export icon of Cookie-Editor
<img src='fig2.png' height=300 width=300>
This will copy the cookie to clipboard.

8. Paste the clipboard to the cookies.json file.

9. Run the following program.
<pre>
import asyncio
from EdgeGPT import Chatbot

async def main():
    bot = Chatbot(cookie_path='cookies.json')
    print(await bot.ask("who is yoshiyasu takefuji?"))
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
</pre>

# Exercise
1. Write a program for interactively asking a question to EdgeGPT and returning the response.

2. Feed the text of "solve x+y=3 and 2x+y=2, and verify it" to your program to show the right answer of x and y.

HINT: 
If incorrect, conversation_style must be set in your program.

3. Write a program to collect a list of peer-reviewed papers on the specific subject.

4. Compare the performance between ChatGPT-3 and EdgeGPT about the above problem.


