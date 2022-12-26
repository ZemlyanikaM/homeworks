from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
from cfg import TOKEN  #токен бота из файда cfg.py
from cfg import OW     #id key openweathermap из файла cfg.py

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
city = "Kursk"
wd = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OW}&units=metric')
data = wd.json()
# print(data['main'])

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("������! ��� ��� � ����:\n\
    ����� ������� /weather � � ������ ���� ������.")


@dp.message_handler(commands=['weather'])
async def weather_message(msg: types.Message):
    await msg.reply(f'�����: {city}\n�����������: {data["main"]["temp"]}\n��������� ���: {data["main"]["feels_like"]}\n��������: {data["main"]["pressure"]}')

if __name__ == '__main__':
    executor.start_polling(dp)
