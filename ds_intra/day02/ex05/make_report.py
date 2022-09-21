from analytics import Research
from config import *


if __name__ == "__main__":
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

    except ValueError as ve:
        print(ve)
    except FileNotFoundError as fnfe:
        print(fnfe)
