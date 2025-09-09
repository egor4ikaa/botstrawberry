from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '8242768529:AAEJtAIvGKvIBSEI7IYTHmx-K5MScSgtX3I'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def process_start_command(message: Message):
    await message.answer("Хэй, меня зовут Эхо-Бот! \nнапиши мне что-нибудь")

async def process_help_command(message: Message):
    await message.answer('Напиши что-нибудь, отправлю в ответ!')

async def process_contact_command(message: Message):
    await message.answer('Не так быстро, мы ещё знакомы!')

async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)

async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)

async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)

async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)

async def send_echo(message: Message):
    await message.reply(text=message.text)

dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(process_contact_command, Command(commands='contact'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_document_echo, F.document)
dp.message.register(send_sticker_echo, F.sticker)

dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)