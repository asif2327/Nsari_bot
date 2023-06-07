from telethon import events 
from .. import bot
from .. import openai_key
from telethon.tl.custom import Button
import asyncio
import openai 
openai.api_key = openai_key
openai_key ="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"
model_engine="gpt-3.5-turbo"

k_board =[[Button.inline("stop and reset", b"stop gpt")]]
@bot.on(events.NewMessage(incoming=True, pattern ="(?i)/ask"))
async def chatgpt(event):
  sender_id = event.sender_id
  gpt_msg= "Hello I Am Ansari Ai that can ansawer to all your queries"
  await bot.send_msg(sender_id, gpt_msg) 
try:
  await bot.send_message(sender_id, gpt_msg)
  async with bot.conversation(await event.get_chat(), exclusive=True, timeout=600)as conv:
    history ={} 
    while True:
      gpt_msg = "Send Your Question"
      u_input = await send_recieve(gpt_msg.conv, k_board)
      if u_input is None:
        gpt_msg="conversation reset.Type/ask to start a new one"
        await bot.send_message(sender_id, gpt_msg)
        break
      else:
        gpt_msg ="I got your question for response"
        ab= await bot.send_message(sender_id, gpt_msg)
        history.append({"role":"user", "content":u_input})
        c_comp= openai.ChatCompletion.create(model=model_engine, 
        message=history, 
        max_tokens=100,
        n=1,
        temperature=0.1,
        )
        response = c_comp.choices[0].message.content
        history.append ({"role":"assistant", "content":response})
        await ab.delete()
        await bot.send_message(sender_id, response, pass_mode="markdown")
except asyncio.TimeoutError:
  await bot.send_message(sender_id, "conversation ended due to no response")
except telethon.errors.AlreadyInConversationError:
  pass
except Exception as e:
  print(e)
  await bot.send_message(sender_id, "conv ended. Something Went Wrong")
  
async def send_recieve(gpt_msg, conv, keyboard):
  msg = await.conv.send_message(got-+_msg, buttns=keyboard)
  done, _ = await asyncio.wait({conv.wait_event(events.CallbackQuery()), conv.get_response()}, return_when=asyncio.FIRST_COMPLETED)
  result = done.pop().result()
  await message.delete()
  
  if isinstance(result, events.CallbackQuer.Event):
    return None
    else:
      return result.message.strip()