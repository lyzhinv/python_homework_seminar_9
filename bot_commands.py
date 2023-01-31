from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello - давай поздароваемся :)\n/time - узнать точное время\n/date - узнать сегодняшюю дату\n/ny - узнать сколько осталось дней до Нового года!\n/sum x y - посчитать сумму двух чисел')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')
  
    
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Точное время - {datetime.datetime.now().time().replace(microsecond=0)}')
    

async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date = datetime.date.today()
    await update.message.reply_text(f'Сегодня - {date.day}.{date.month}.{date.year}')
    
    
async def ny_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ny_2024 = datetime.date(2024, 1, 1)
    current_day = datetime.date.today()
    await update.message.reply_text(f'До Нового 2024 года осталось {(current_day - ny_2024).days} дней(я)')
    
    
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    if x is None or y is None:
        print('Error')
    await update.message.reply_text(f'sum {x} + {y} = {x + y}')