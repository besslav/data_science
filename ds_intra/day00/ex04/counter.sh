#!/bin/sh
echo '"name","count"' > hh_uniq_positions.csv

mid=$(grep -o -i Junior hh_positions.csv |wc -l)
echo '"Junior"', $mid > test.csv
mid=$(grep -o -i Middle hh_positions.csv |wc -l)
echo '"Middle"', $mid >> test.csv
mid=$(grep -o -i Senior hh_positions.csv |wc -l)
echo '"Senior"', $mid >> test.csv

sort -t ',' -rk 2 test.csv >> hh_uniq_positions.csv
rm test.csv