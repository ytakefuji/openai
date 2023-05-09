# openai
There are two types of dialog AI systems: online interactive dialog AI via browser and online terminal command AI in batch style. To use online terminal command AI, their settings are required respectively.

This repository will introduce three types of AI: ChatGPT-3 with Openai, EdgeGPT with Microsoft and Google Bard. 

The following links are online interactive dialog AI systems:

https://chat.openai.com/

https://bard.google.com/

https://bing.com/chat

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

The temperature is a determinant of randomness from 0.0 to 1.0 to control the randomness. The larger the temperature, the greater the randomness.

2. Write a english-to-japanese translator.

3. Write a program to collect a list of peer-reviewed papers on the specific subject.


# EdgeGPT
EdgeGPT takes advantage of the new version of Bing (Microsoft search engine)
with ChatGPT-3.5 or 4.0.

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
0. Make sure cookie-editor in edge browser showing your cookies, not empty. To show the content of cookie-editor, after logging into your Microsoft account at the Edge, you will need to access bing.com.

1. Write a program for interactively asking a question to EdgeGPT and returning the response.

2. Give the text of "solve x+y=3 and 2x+y=2, and verify it" to your program to show the right answer of x and y.

HINT: 
If incorrect, conversation_style must be set in your program.

3. Give the text "show email for yoshiyasu takefuji" to show the right email address.

4. Write a program to collect a list of peer-reviewed papers on the specific subject.

5. Compare the performance between ChatGPT-3 and EdgeGPT about the above problem.

# Google search console API example
1. Create your Google Cloud account and enable custom search to obtain your unique API key.
https://console.cloud.google.com/cloud-resource-manager

2. Enable custom search service. To obtain Google CSE ID, access to https://cse.google.com.

<pre>
from googleapiclient.discovery import build
import json

GOOGLE_CSE_ID='your unique cx'
GOOGLE_API_KEY='enabled search API KEY'
API_SERVICE_NAME = 'searchconsole'

def gsearch(keyword, num=10):
    search_service = build("customsearch","v1",developerKey=GOOGLE_API_KEY)
    response = search_service.cse().list(
                q=keyword,
                cx=GOOGLE_CSE_ID,
                lr='lang_en',
                num=num,
                start=1
            ).execute()
    res = json.dumps(response, ensure_ascii=False, indent=4)    print(res)

if __name__ == '__main__':
    keyword = input("enter your question: ")
    gsearch(keyword)
</pre>

# Exercise
1. Run the above code.

2. Create a new application with Google search API and EdgeGPT API.

# Bard by Google
Access to https://bard.google.com/

1. ask "who is yoshiyasu takefuji with a google search command "yoshiyasu takefuji".

2. ask "who is yoshiyasu takefuji with a google phrase search command "yoshiyasu takefuji".

3. ask 'use google search with a search phrase command "yoshiyasu takefuji" and find who is yoshiyasu takefuji.'

4. use the google search phrase-site-command with "yoshiyasu takefuji site:nih.gov" and show the result of publications published after 2021 with single-authored as many as possible and verify them with obtained DOIs respectively.

# BARD from terminal command line

1. Access to https://bard.google.com/ with Chrome and use cookie-editor to get "__Secure-1PSID".

2. export BARD_QUICK="true"

3. export BARD_SESSION= <value of "__Secure-1.PSID">

4. pip install GoogleBard

5. run the following command on terminal:

$ python -m Bard "use google phrase search with 'yoshiyasu takefuji' and find who is yoshiyasu takefuji?"

# Exercises
1. Interacting with ChatGPT, EdgeGPT and Bard respectively makes a cookie editor 
in Python for Chrome on your operating system to show all information of cookies and extract 
the value of "__Secure-1.PSID".

2. Compare their performance.

3. Make an exciting application in Python with interacting online dialog AI such as ChatGPT, EdgeGPT or Bard.

Hints: 

A. Understanding text in English with ChatGPT-4 is 85.5% while one in Japanese is 79.9%.

B. You need to choose right words and phrases in dialog with AI (ChatGPT, EdgeGPT and Bard).

C. Multiple conversations may be necessary.
