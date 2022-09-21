from analytics import Research
from config import *
import logging
import requests
import json


def telegram_bot_sendtext(bot_message):
    logging.info("telegram_bot_sendtext()")
    bot_token = '5758739250:AAGymo213uuzWfkRjEt5OxZ2CX1H-jmbO-4'
    bot_chatID = '401825621'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.post(send_text)


if __name__ == "__main__":
    logging.basicConfig(filename='report.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

    try:
        m = Research(file_with_data)
        list_data = m.file_reader()
        calculation_init = m.Calculations(list_data)
        counted = calculation_init.counts()

        fract_count = calculation_init.fractions(counted)

        pred = m.Analytics(file_with_data).predict_random(num_of_steps)
        pred_counted = m.Analytics(pred).counts()
        report = report_line.format(len(list_data), counted[1], counted[0], round(fract_count[1], 2),
                                    round(fract_count[0], 2), num_of_steps, pred_counted[1], pred_counted[0])
        m.Analytics(list_data).save_result(report, result_file, res_file_type)
        telegram_bot_sendtext(success)

    except Exception as ee:
        telegram_bot_sendtext(unsuccess)
        print(ee)

#401825621