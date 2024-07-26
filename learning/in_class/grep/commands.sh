# 1
cat review.csv | grep quality

# 2
grep -i francisco hamlet.txt

#3
grep -io battery review.csv | wc -l

#4
grep -in excellent review.csv

#5
grep -iv the hamlet.txt

#6
grep -iE "design|performance" review.csv
grep -i "design\|performance" review.csv

#7
grep -ohE "battery|Battery" review.csv
grep -ohE "[b|B]attery" review.csv

#8
grep -i sick $(find *.txt)

#9
grep -iE "\bb[a-zA-z]*y\b" review.csv
