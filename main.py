import Constants as keys
from telegram.ext import *
import Responses as R
import OpenAI
from selenium import webdriver


'''
def prenota_command(update, context):
    update.message.reply_text('Ecco la prenotazione')

'''
print("bot started...")

def calcola_totale():
    print(variabile_che_non_esiste + 5) 

# 2. F706: Return outside function (Errore di sintassi logica)
# Decommenta la riga sotto per testare l'errore fatale di sintassi
return "Sono fuori da una funzione" 

# 3. F632: Use of 'is' for literal (Bug logico frequente)
s = "ciao"
if s is "ciao":  # Questo DEVE attivare F632
    print(s)

# 4. F704: Yield outside function
yield 10 

# 5. E999: Syntax Error puro (Indentazione errata o parentesi chiuse male)
def errore_sintassi():
  print("Parentesi non chiusa")

def start_command(update, context):
    update.message.reply_text("Sti gran cazzi!!")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.todayPren_resp(text)
    print(response)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # dp.add_handler(CommandHandler("prenota", prenota_command))
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
