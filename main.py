from aiogram import Bot,Dispatcher,types,executor
import config
import sqlite3
import random

bot = Bot(token = config.token)
dp = Dispatcher(bot)

connect = sqlite3.connect('users.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id_user INTEGER,
    chat_id INTEGER
    );
    """)
connect.commit()
@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO users VALUES ('{message.from_user.username}',
    '{message.from_user.first_name}', '{message.from_user.last_name}',
    {message.from_user.id}, {message.chat.id})""")
    connect.commit()
    await message.answer(f"Здраствуйте {message.from_user.full_name}")
# @dp.message_handler()
#Homework

@dp.message_handler(commands=['azino777'])
async def azino777(message:types.Message):
    await message.answer("Угадай число 1:3")

@dp.message_handler(text= [1,2,3])
async def azino(message:types.Message):
    azi= random.randint(1,3)
    answer = int(message.text)
    
    if answer == azi:
        await message.reply(f"Вы угадали {azi}")
        # await message.answer(azi)
    else:
        await message.answer ("Вы не угадали")
        await message.answer(f"правильное число: {azi}" )


executor.start_polling(dp)

#Homework

