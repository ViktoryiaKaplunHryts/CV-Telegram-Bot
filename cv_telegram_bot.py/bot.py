#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'Вставить TOKEN'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.InlineKeyboardMarkup(row_width=4)
	item1 = types.InlineKeyboardButton("💥 Резюме", url='https://drive.google.com/file/d/1UDLUWFXfNfH5GKeCVC8NC2WE7EpJQqg9/view?usp=sharing')
	item2 = types.InlineKeyboardButton("💥 Сайт", url='https://viktoryiakaplunhryts.github.io/')
	item3 = types.InlineKeyboardButton("💥 Github", url='https://github.com/ViktoryiaKaplunHryts')
	item4 = types.InlineKeyboardButton("💥 Telegram", url='https://t.me/Victoryia_Kaplun_Hryts')
	item5 = types.InlineKeyboardButton("💥 LinkedIn", url='https://www.linkedin.com/in/victoryia-kaplun-hryts-qa-engineer/')
	

	markup.add(item1, item2,item3,item4,item5)

	bot.send_message(message.chat.id, "<b>Добро пожаловать, уважаемый HR!</b>\n\nЕсли ты в поиске QA Engineera готового в кратчайшие сроки на 100% погрузиться в проект, быстро влиться в коллектив и плечом к плечу сражаться за высочайшее качество продукта, то давай знакомиться - меня зовут <b>Виктория</b>.\n\nЯ активный и высокомотивированный инженер по тестированию. Стремлюсь к постоянному саморазвитию и обучению, считаю важным двигаться вперёд и не останавливаться на достигнутом, что и стало причиной ухода с должности судебного исполнителя.\n\nВ работе предпочитаю принцип честности и открытости. Способна эффективно выполнять большой объем разноплановых задач. \n\n💥 Мой принцип работы - 'чего не знаю - найду, чего не найду - спрошу'💥. \n\nИмею высокий уровень стрессоустойчивости, которой позавидуют монахи Шаолиня ( и снова «привет» работе судебного исполнителя 😊 ). \n\nИ наконец, я люблю стендап.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)













#https://core.telegram.org/bots/api#available-methods
