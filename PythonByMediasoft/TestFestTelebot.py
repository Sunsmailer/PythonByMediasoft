
import telebot

bot = telebot.TeleBot("место для вашего токена от фавер отца")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "привет" or message.text == "<<Привет>>" or message.text == "<<привет>>" or message.text == "Ghbdtn" or message.text == "ghbdtn":
        bot.send_message(message.from_user.id,
                         "  Привет, чем я могу тебе помочь? \n \n     Список доступных команд: \n 🍏 Когда фест \n 🍊 Последний фест \n 🥝 Соцсетка")
    elif message.text == "Когда фест" or message.text == "когда фест" or message.text == "Когда фест?" or message.text == "когда фест?":
        bot.send_message(message.from_user.id,
                         "Ближайщий фестиваль MIZUKI FEST пройдет 19 июня в Димитровграде. Начало в 14.00. Подать заявку на участие или узнать более подробную информацию можно  в группе Тестфеста: https://vk.com/testfest.ulsk")
    elif message.text == "Последний фест" or message.text == "последний фест" or message.text == "Последний" or message.text == "последний":
        bot.send_message(message.from_user.id,
                         "Последний фестиваль проходил 22 мая, подробности здесь: https://vk.com/eos.fest")



    elif message.text == "Соцсетка" or message.text == "соцсетка":
        bot.send_message(message.from_user.id,
                         "Наши соцсети: \nВк: https://vk.com/testfest.ulsk \nИнстаграмм: https://www.instagram.com/tf.ulsk_team/ \nДискорд: https://discord.com/invite/xPAJFdG")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, '''Напиши боту "Привет"''')
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=5)

