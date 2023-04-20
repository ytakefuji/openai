import asyncio
from EdgeGPT import Chatbot
f=open('reply','w')

async def main():
    bot = Chatbot(cookie_path='cookies.json')
    res=(await bot.ask("who is yoshiyasu takefuji?"))
    print(res,file=f)
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
    f=open('reply','r')
    print(f.read().split('text')[2])
