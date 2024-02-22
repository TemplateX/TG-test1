print('qq1')
#telegram
#import asyncio
from pyrogram import Client, filters
# 51.79.229.202:3128

app = Client("my_account", api_id="21058377", api_hash="4d286f050f73dd5f372d423304331886")
session_string = 'AgFBU0kAdqeZ5dyes4h16vy3KxMrOEsBX2Z4ulHPBwXYiFLnciqL6IM0azIo8iAITv8XpOoKo7K6pGf07f4bOADHkay2ln3n3hqymAx2UZ9sUffSfrhKnhX5NwtjyxLihXirjNXV4WJkCgNb-_p7x1JczV6taO0YQr04gW31C9GGDjZ8PLAdhz7Hayxdcruwska0iZACNt6yezlyPzp5vcsn-H_IiFjp88LPAGGBgCWT-IANUMLDg47FUzqf6AIPN8R45htteazWOk8iGODclrti3yIqXdpBO3DgTDc13W3nWnfZEZhozwc8momdZwefYIo9xP1Y09vekiwSkPlRsS5lLVoTpQAAAAA3cDxDAA'

async def main():
  async with Client("my_account", session_string=session_string) as app:
      #print(await app.export_session_string())
      print('inside_qq')
      print(await app.get_me())

app.run(main())  # Automatically start() and idle()
