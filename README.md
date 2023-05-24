# How to use generative AI systems
This is under review.

This is a tutorial on how to use generative AI systems for Data Science at Musashino University in Japan.

There are two types of dialog generative AI systems: online interactive dialog AI via browser and terminal command AI in batch style. To use terminal command AI, their settings are required respectively.

This repository will introduce six types of dialog AI systems: ChatGPT-3 with/without browser, Bing.com via Edge or EdgeGPT without browser, and Google Bard with/without browser. EdgeGPT is based on ChatGPT-4: https://blogs.bing.com/search/march_2023/Confirmed-the-new-Bing-runs-on-OpenAI%E2%80%99s-GPT-4

The following three links are online interactive dialog AI systems via browser for free of charge:

ChatGPT-3 via any browser: https://chat.openai.com/

Bard via any browser: https://bard.google.com/

Bing.com via Edge browser using ChatGPT-4: https://bing.com/chat

<b>
You need to practice interacting with the AI to accomplish the required tasks. Practice makes perfect.
</b>

# Simple examples via browser

1. Query to AI: show a code in Python to display a graph with data.csv 
   composed of x and y determinants.
<pre>
Answer from AI:
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
x = data['x']
y = data['y']

plt.plot(x, y)
plt.show()
</pre>

2. Query to AI: who is yoshiyasu takefuji?
<pre>
Answer from AI:
Yoshiyasu Takefuji is a professor at **Musashino University** in the **Data Science** department². He has a Ph.D. and his research interests include cyber-security, machine learning, neural computing, energy harvesting, IoT, automated reasoning, and applied AI². He has developed AI prototypes that outperform super-skilled humans in civil engineering and construction, marketing, skin cancers, and many other areas². Is there anything else you would like to know about him?

Source: Conversation with Bing, 2023/5/13
(1) Yoshiyasu TAKEFUJI | Professor | Ph.D. Professor .... https://www.researchgate.net/profile/Yoshiyasu-Takefuji.
(2) 武藤 佳恭 (Takefuji Yoshiyasu) - マイポータル - researchmap. https://researchmap.jp/ytakefuji.
(3) ytakefuji (Yoshiyasu Takefuji) · GitHub. https://github.com/ytakefuji.
</pre>
Hint:
If AI does not respose to your query well, add an extra word such as Professor or Dr. in your dialog. In other words, ask "who is Professor yoshiyasu takefuji?" 

3. Query to AI: show a list of publications by yoshiyasu takefuji in 2023.
<pre>
Answer from AI:
I’m sorry, but I couldn’t find any specific information about publications by Yoshiyasu Takefuji in 2023. Would you like to know about his publications from another year or more general information about his work?
</pre>
4. Query to AI: show a list of publications by yoshiyasu takefuji in 2023 
   with google query command of "yoshiyasu takefuji site:nih.gov after:2023-1-1"
<pre>
Answer from AI:
hiscovid for visualizing and identifying when policymakers made mistakes against COVID-19
doi: 10.1016/j.simpa.2023.100466

Review of hikikomori: A global health issue, identification and treatment
doi: 10.1016/j.ajp.2023.103596
</pre>
5. Query to AI: summarize them.
<pre>
Answer from AI:

hiscovid for visualizing and identifying when policymakers made mistakes against COVID-19

This paper presents a new tool called hiscovid that can be used to visualize and identify when policymakers made mistakes against COVID-19. hiscovid uses a time-series policy outcome scoring tool to evaluate the outcomes of COVID-19 policies by country. The daily cumulative population mortality is used for scoring the outcomes of COVID-19 country policies. hiscovid allows policymakers to observe the progress and transition of scores over time to learn lessons from the past decision-making mistakes for correcting the current policies to reduce unnecessary deaths.

Review of hikikomori: A global health issue, identification and treatment

This paper reviews the literature on hikikomori, a Japanese term for a condition in which people withdraw from social contact and isolate themselves in their homes for extended periods of time. Hikikomori is a global health issue, with an estimated 1.5 million people in the United States and 1.2 million people in Europe affected by the condition. The paper discusses the identification and treatment of hikikomori, and provides recommendations for future research.
</pre>

6. Draw the age group circles where the center point of each circle indicates the average of HbA1c, and the size of each circle is the number of participants after calculating the average HbA1c for each age group with the following dataset.

Download the dataset from the following site:

https://data.mendeley.com/datasets/g7gzwd4c7h

Reference: Maw, Su Su; Haga, Chiyori (2018), “Dataset for lifestyle behaviors and HbA1c status from 2012 to 2014 of Japanese middle aged and elder people”, Mendeley Data, V1, doi: 10.17632/g7gzwd4c7h.1


ask AI to show a code in Python to create and save a graph of "HbA1c" vs "Age" with the downloaded dataset: data.csv. Calculate the average HbA1c for each age group and draw a circle for each age group. The center point of the circle indicates the average of HbA1c, and the size of the circle is the number of participants in the age group.


Hint:
The range of "Age" values is from 40 to 74. The range of "HbA1c" values is from 3.5 to 12.9. 

The following diagram is produced by the AI-created program in Python.

<img src="https://github.com/ytakefuji/openai/blob/main/hbA1c_vs_age.png" height=240 width=320>

7. Make a code in Python to visualize military spending of up to 4 countries from 2000 to 2022
   with the following xlsx file. 4 lines of the graph is colored with black and white.

https://www.sipri.org/sites/default/files/SIPRI-Milex-data-1949-2022.xlsx

Hint: explain to AI on how to extract the important data from the xlsx file to visualize time-series data of up to 4 countries.


# Challenging EXAMPLES

1. This is called a pangram generator. Use all 26 lowercase letters of the alphabet only once to create a meaningful sentence. This is a difficult problem!

Answer from AI should be:

Sphinx of black quartz, judge my vow.

Pack my box with five dozen liquor jugs.

The five boxing wizards jump quickly.

The quick brown fox jumps over lazy dog.


2. Design a 3-input 3-output combination logic circuit that negates the 3 input signals. Any number of AND and OR gates can be used, but only two NOT gates are allowed.

<pre>
Input	Output
000	111
001	110
010	101
011	100
100	011
101	010
110	001
111	000
</pre>

3. Write a code in Python to solve the 12-coin-3-weighing puzzle. In 12-coin-3-weighing puzzle, twelve coins are given where eleven of which are identical. If one is different, we don't know whether it is heavier or lighter than the others. The balance may be used three times to determine if there is a unique (counterfeit or fake) coin to isolate it and determine its weight relative to the others.

# Teriminal command AI with ChatGPT

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
1. Interacting with ChatGPT generates a program (ask.py) in Python for interactively asking user's question and the temperature setting with ChatGPT and returning the response.

Hint: The temperature is a determinant of randomness from 0.0 to 1.0 to control the randomness. The larger the temperature, the greater the randomness.

2. Create a english-to-japanese translator in Python by ChatGPT.

3. Create a program to collect a list of peer-reviewed papers on the specific subject given from a user.


# EdgeGPT from terminal command
EdgeGPT takes advantage of the new version of Bing (Microsoft search engine)
with ChatGPT-4.0. The installation of EdgeGPT is detailed as follows.

1. $ pip install EdgeGPT

2. Install the latest Edge browser.

3. With Edge, open https://bing.com/chat site.

4. Install Cookie-Editor for Edge.

5. Make sure accessing bing.com with Edge.

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

1. Write a program (edge.py) for interactively asking a question to EdgeGPT and returning the response.

2. Give the text of "solve x +  y = 3 and 2 x + y = 2, and verify it" to your program until the answer shows the right answer of x and y.

HINT: 
If you have incorrect results, conversation_style must be set in your program.

3. Give the following text "show email for yoshiyasu takefuji" to show the right email address.

4. Write a program in Python to collect a list of peer-reviewed papers on the specific subject.

5. Compare the performance between ChatGPT-3 and EdgeGPT about the above problem.

# Google search console API example
The Google search capability for the latest information can be used with AI to strengthen the wiser system.

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

2. Create a new application with combining Google search API and EdgeGPT API.

# Bard by Google via browser
Access to https://bard.google.com/

1. ask "who is yoshiyasu takefuji with a google search command "yoshiyasu takefuji".

2. ask "who is yoshiyasu takefuji with a google phrase search command "yoshiyasu takefuji".

3. ask 'use google search with a search phrase command "yoshiyasu takefuji" and find who is yoshiyasu takefuji.'

4. use the google search phrase-site-command with "yoshiyasu takefuji site:nih.gov" and show the result of publications published after 2021 with single-authored as many as possible and verify them with obtained DOIs respectively.

5. make a new interesting application with Bard.

# BARD from terminal line command

1. Access to https://bard.google.com/ with Chrome and use cookie-editor to get "__Secure-1PSID".

2. export BARD_QUICK="true"

3. export BARD_SESSION= <value of "__Secure-1PSID">

4. pip install GoogleBard

5. run the following command on terminal:

$ python -m Bard "use google phrase search with 'yoshiyasu takefuji' and find who is yoshiyasu takefuji?"

# Exercises
1. Interacting with ChatGPT, Bing.com or EdgeGPT, and Bard respectively makes a cookie editor 
in Python for Chrome on your operating system to show all information of cookies and extract 
the value of "__Secure-1PSID".

2. Compare their performance.

3. Solve it: x + y = 3 and 2 x + y = 2.

4. Make an exciting application in Python with interacting generative AI such as ChatGPT, bing.com or EdgeGPT, or Bard. All conversations with the AI should be noted and the conversations will be included in the comments before the generated program. The new and exciting features of the result generated by your program using generative AI should be clearly stated.

Hints: 

A. Understanding text in English with ChatGPT-4 is 85.5% while one in Japanese is 79.9%.

B. You need to choose right words and phrases in dialog with AI (ChatGPT, EdgeGPT and Bard). Add extra words and/or phrases in your dialog.

C. Multiple conversations may be necessary.
