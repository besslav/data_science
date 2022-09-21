#! /bin/sh


python3 -m cProfile  financial.py 'MSFT' 'Total Revenue' > profiling-sleep.txt
python3 -m cProfile  financial.py 'MSFT' 'Total Revenue' > profiling-tottime.txt
python3 -m cProfile  financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-http.txt
python3 -m cProfile -s ncalls financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-ncalls.txt
# Скрипты записывают результаты в файл


# Скрипт со
python3 -m cProfile -s ncalls -o pstats-cumulative.temp financial_enhanced.py 'MSFT' 'Total Revenue'
python3 -m pstats pstats-cumulative.temp   
% sort cumulative
% stats 5