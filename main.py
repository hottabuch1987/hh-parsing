from dotenv import load_dotenv
from os import environ
from work import array
import csv
import telebot

load_dotenv()


FILE_CSV = "/Users/hottabych/Desktop/parsing/data.csv"


def main(parametr):
    # Сохранение в CSV
    with open(FILE_CSV, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Название", "Зарплата", "Опыт", "URL"])
        for item in parametr():
            print(item)
            csv_writer.writerow(item)




def send_file():
    # Функция отправки файла через телеграм
    API_KEY = environ.get('API_KEY')
    CHAT_ID = environ.get('CHAT_ID')
    bot = telebot.TeleBot(API_KEY)

    with open(FILE_CSV, 'rb') as f:
        bot.send_document(CHAT_ID, f)



if __name__ == "__main__":
    main(array)
    send_file()


