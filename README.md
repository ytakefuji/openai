![image](https://github.com/ytakefuji/openai/assets/12127408/ecd3f835-0e6e-4b6c-9e67-77221dcbcc56)# How to use generative AI systems 

Takefuji, Y. A brief tutorial on generative AI. Br Dent J 234, 845 (2023). https://doi.org/10.1038/s41415-023-6041-0


This is under review.

This is a tutorial on how to use generative AI systems such as Bing.com with ChatGPT-4 and Bard for Data Science at Musashino University in Japan.

There are two types of dialog generative AI systems: online interactive dialog AI via browser and terminal command AI in batch style. To use terminal command AI, their settings are required respectively.

This repository will introduce six types of dialog AI systems: ChatGPT-3 with/without browser, Bing.com via Edge with ChatGPT-4 or EdgeGPT without browser, and Google Bard with/without browser. EdgeGPT is based on ChatGPT-4: https://blogs.bing.com/search/march_2023/Confirmed-the-new-Bing-runs-on-OpenAI%E2%80%99s-GPT-4

The following three links are online interactive dialog AI systems via browser for free of charge:

ChatGPT-3 via any browser: https://chat.openai.com/

Bard via any browser: https://bard.google.com/

Bing.com via Edge browser using ChatGPT-4: https://bing.com/chat

<b>
You need to practice interacting with the AI to accomplish the desired tasks. Practice makes perfect.
</b>

# Examples via browser

The difficulty level is indicated by the number of asterisks (*). The more asterisks, the higher the difficulty. 

<b>
1. Query to AI: show a code in Python to display a graph with data.csv 
   composed of x and y determinants.
</b>

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
<b>
2. Query to AI: who is yoshiyasu takefuji?
</b>
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

<b>
3. Query to AI: show a list of publications by yoshiyasu takefuji in 2023.
</b>
<pre>
Answer from AI:
I’m sorry, but I couldn’t find any specific information about publications by Yoshiyasu Takefuji in 2023. Would you like to know about his publications from another year or more general information about his work?
</pre>
<b>
4. Query to AI: show a list of publications by yoshiyasu takefuji in 2023 
   with search query command of "yoshiyasu takefuji site:nih.gov after:2023-1-1"
</b>
<pre>
Answer from AI:
hiscovid for visualizing and identifying when policymakers made mistakes against COVID-19
doi: 10.1016/j.simpa.2023.100466

Review of hikikomori: A global health issue, identification and treatment
doi: 10.1016/j.ajp.2023.103596
</pre>
<b>
5. Query to AI: summarize them.
</b>
<pre>
Answer from AI:

hiscovid for visualizing and identifying when policymakers made mistakes against COVID-19

This paper presents a new tool called hiscovid that can be used to visualize and identify when policymakers made mistakes against COVID-19. hiscovid uses a time-series policy outcome scoring tool to evaluate the outcomes of COVID-19 policies by country. The daily cumulative population mortality is used for scoring the outcomes of COVID-19 country policies. hiscovid allows policymakers to observe the progress and transition of scores over time to learn lessons from the past decision-making mistakes for correcting the current policies to reduce unnecessary deaths.

Review of hikikomori: A global health issue, identification and treatment

This paper reviews the literature on hikikomori, a Japanese term for a condition in which people withdraw from social contact and isolate themselves in their homes for extended periods of time. Hikikomori is a global health issue, with an estimated 1.5 million people in the United States and 1.2 million people in Europe affected by the condition. The paper discusses the identification and treatment of hikikomori, and provides recommendations for future research.
</pre>
<b>
6.** Draw the age group circles where the center point of each circle indicates the average of HbA1c, and the size of each circle is the number of participants after calculating the average HbA1c for each age group with the following dataset.
</b>

Download the dataset from the following site:

https://data.mendeley.com/datasets/g7gzwd4c7h

Reference: Maw, Su Su; Haga, Chiyori (2018), “Dataset for lifestyle behaviors and HbA1c status from 2012 to 2014 of Japanese middle aged and elder people”, Mendeley Data, V1, doi: 10.17632/g7gzwd4c7h.1


ask AI to show a code in Python to create and save a graph of "HbA1c" vs "Age" with the downloaded dataset: data.csv. Calculate the average HbA1c for each age group and draw a circle for each age group. The center point of the circle indicates the average of HbA1c, and the size of the circle is the number of participants in the age group.


Hint:
The range of "Age" values is from 40 to 74. The range of "HbA1c" values is from 3.5 to 12.9. 

The following diagram is produced by the AI-created program in Python.

<img src="https://github.com/ytakefuji/openai/blob/main/hbA1c_vs_age.png" height=240 width=320>

<b>
7.0* Show a full code in Python to draw a graph of 4 country lines from 2000 to 2022 with SIPRI-Milex-data-1949-2022.csv
</b>

Hint: Identify 'Country' column name.

https://github.com/ytakefuji/openai/blob/main/SIPRI-Milex-data-1949-2022.csv

<b>
7.1** Make a code in Python to visualize military spending of up to 4 countries from 2000 to 2022
   with the following xlsx file. 4 lines of the graph is colored with black and white. User is allowed to enter up to 4 countries from the terminal.
</b>


https://www.sipri.org/sites/default/files/SIPRI-Milex-data-1949-2022.xlsx

Hint: explain to AI on how to extract the important data from the xlsx file to visualize time-series data of up to 4 countries.

<b>
8.* Solve it using real numbers and complex numbers respectively: x - 2y = 0 and x^2 - y^2 = -3.
</b>

Hint: no hint.

<b>
9.* Draw a US-state map with red Oregon, blue California, green Florida, yellow New York and lightgray others.
</b>

Hint: use geopandas.

<img src='usmap.png' width=414 height=260>

<b>
10.** Draw a Japan-prefecture map with green Hokkaido, blue Iwate, red Tokyo, yellow Kagoshima and lightgray others.
</b>

<img src='japan.png' width=576 height=432>

Hint: use geopandas and find a Japan prefecture map.

<b>
11.**** show two codes in Python how to upload and download a csv file on your account of Facebook, LinkedIn or Line for sharing it within group members while the current SNS platforms do not allow users to upload/download a csv file. There is no menu to upload a csv file.
</b>

Hint: no hint.

<b>
12.** Find 6-letter lowercase words of the alphabet without "aeiou" and 5-letters lowercase words without "aeiou". A word should not contain a repeated letter.
</b>

Hint: no hint.

<b>
13.** Use the following datasets on the global temperature and CO2. Calculate the correlation and discuss the global warming with human-induced CO2.　Don't be preconceived in research
</b>

Use the following site which contains the latest data with every month updated.

https://www.ncei.noaa.gov/data/noaa-global-surface-temperature/v5.1/access/timeseries/

The following link is lost.

https://www.ncei.noaa.gov/data/noaa-global-surface-temperature/v5.1/access/timeseries/aravg.mon.land_ocean.90S.90N.v5.1.0.202304.asc

https://www.ncei.noaa.gov/data/noaa-global-surface-temperature/v5.1/access/timeseries/aravg.mon.land_ocean.90S.90N.v5.1.0.202305.asc

Use the global monthly co2 data:

ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.csv
 
<img src="https://github.com/ytakefuji/openai/blob/main/GlobalTemp.png" height=300 width=500>

<img src="https://github.com/ytakefuji/openai/blob/main/contradict.png" height=400 width600>

Hint:

1. convert co2_mm_mlo.csv to co2.csv with three columns such as 'year', 'month' and 'mean'.

2. Cope with monthly updated file-name changes to download the correct latest data.

3. Similarily, convert aravg.mon.land_ocean.90S.90N.v5.1.0.202305.asc to temp.csv with three columns such as 'year', 'month' and 'change'.

4. plot a graph of two lines of co2 and temperature from 1940 to 1967.

<b>
14.** Make a scorecovid application for calculating scores of selected countires with dividing the number of cumulative deaths by the population per million and sorting scores in ascending order.
</b>
   
Many COVID-19 datasets are not being updated anymore. However, WHO is now handling COVID-19 dataset:
https://covid19.who.int/WHO-COVID-19-global-data.csv

Use the population data at:
https://github.com/ytakefuji/score-covid-19-policy/raw/main/country-pop.csv

<pre>
$ scorecovid
Latest date: 2023-06-07
             country  population  deaths  score
United Arab Emirates     9441129    2349    248
         New Zealand     5185288    2942    567
               Japan   123951692   74694    602
             Iceland      372899     260    697
           Australia    26177413   21063    804
              Canada    38454327   52645   1369
              Israel     9038309   12540   1387
             Germany    83369843  174412   2092
              Sweden    10549347   24371   2310
              France    64626628  163680   2532
              Brazil   215313498  702907   3264
       United States   338289857 1127152   3331
      United Kingdom    67508936  226645   3357
             Hungary     9967308   48789   4894
</pre>

<b>
15.*** Draw a graph based on Bayesian theory to calculate the probability of detecting someone is positive. 
</b>

Assume that the probability of individual with disease is 0.065 and non-infected population probability is 0.935. 

Assume the true positive rate of testing is 0.991 and the false positive rate is 0.0005. 
Formulate the probability of detecting someone is positive: P(x,y) where x and y are the false positive rate and the true positive rate respectively.

Hint: no hint


<b>
16.** Use rows.csv: https://data.cdc.gov/api/views/3rge-nu2a/rows.csv and 
show the effectiveness of vaccination with symptoms by age groups.
</b>


Hint: no hint


<b>
17.* draw a graph of the following with data.csv.
</b>

<pre>
$ cat data.csv
factor,value
A,5
A,7
A,8
B,2
B,4
B,6
C,1
C,3
C,5
</pre>

<img src="https://github.com/ytakefuji/openai/blob/main/plot.png?raw=true" width=320 height=240>

Hint: Each boxplot in a graphical indicates representation of the distribution of a dataset with the median, quartiles, and outliers of the data.

<b>
18.* Draw a graph of the following csv file without modifying csv contents.
</b>

use [medicare.csv](https://github.com/ytakefuji/openai/blob/main/medicare.csv)

The result should be shown.

<img src='medicare.png' width=320 height=240>

<pre>
$ cat medicare.csv
Year,PERM Cycles Included,Estimated Improper Payments (in billions),Overall Rate,FFS Rate,Managed Care Rate,Eligibility Rate
2010,Cycle 2 – FY 2007,$22.50 ,9.40%,4.40%,1.00%,5.90%
,,,,,,
,Cycle 3 – FY 2008,,,,,
,,,,,,
,Cycle 1 – FY 2009,,,,,
2011,Cycle 3 – FY 2008,$21.90 ,8.10%,2.70%,0.30%,6.00%
</pre>

<b>
19.** Breast cancer screening between 1994-2009 and 2007-2013. 
   Use two sites and discuss false-positive and accuracy for comparison.
</b>

https://tools.bcsc-scc.org/dataexplorer/

https://www.bcsc-research.org/statistics/diagnostic-performance-benchmarks/diagnostic-mammography-sensitivity-specificity

Hint: pick 'Exam' for "Count by" and 'Screening mammogram classification' for "Screening mammography performance and cancer rates" for 1994-2009. 
Calculate false-positive and accuracy for 2007-2013.


<b>
20.* Predict cross-validation accuracy of binary classification of 'Group' in the dataset.
   And show top-5 feature importances.
</b>

https://dfzljdn9uc3pi.cloudfront.net/2022/14078/1/raw_data.csv

<b>
21.* What is the probability that she actually has breast cancer with positive mammogram? 
</b>

1% of women at age forty who participate in routine screening have breast cancer. 80% of women with breast cancer will get positive mammograms. 9.6% of women without breast cancer will also get positive mammograms. A woman in this age group had a positive mammography in a routine screening. 

Hint: Bayesian theory


# Challenging EXAMPLES
<b>
1.***** This is called a perfect pangram generator. Use all 26 lowercase letters of the alphabet only once to create a meaningful sentence. This is a difficult problem!
</b>
   
Answer from AI should be:

Mr. Jock, TV quiz Ph. D., bags few lynx.

Cwm fjord bank glyphs vext quiz.

<b>
We finally made a pangram generator and created new perfect pangrams.

1. Fez, Jud know strych pilm, vag BQX.

strych pilm=dust at the attic, to vag = to trail on the ground, BQX=Brooklyn Queens Connector
   
2. TCK, Find sphex jow, glazy bum, QRV?

TCK=third culture kid, sphex=insect, jow= hit or strike, bum=british slang: buttocks, QRV=are you ready?
   
3. V? Pry jokish cwm, flag bed, Untz QX?

V=to show sarcasm or humor, pry=inquire, cwm (chat with me), flag=relax, Untz=electric drum sound, QX=Roger
</b>

<b>
2.***** Design a 3-input 3-output combination logic circuit that negates the 3 input signals. Any number of AND and OR gates can be used, but only two NOT gates are allowed.
</b>
   
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
<b>
3.**** Write a code in Python to solve the 12-coin-3-weighing puzzle. In 12-coin-3-weighing puzzle, twelve coins are given where eleven of which are identical. If one is different, we don't know whether it is heavier or lighter than the others. The balance may be used three times to determine if there is a unique (counterfeit or fake) coin to isolate it and determine its weight relative to the others.
</b>
   
# Terminal command AI with ChatGPT

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

B. You need to choose right words and phrases in dialog with AI (ChatGPT-3, bing.com with ChatGPT-4 and Bard). Add extra words and/or phrases in your dialog.

C. Multiple conversations may be necessary.

https://www.nature.com/articles/s41433-023-02563-3/figures/1

<img src='https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41433-023-02563-3/MediaObjects/41433_2023_2563_Fig1_HTML.png' width=400 height=400>
