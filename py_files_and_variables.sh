#!/bin/bash

#declaring an empty array
declare -a data

#reading the data from the external file and putting each line inside the array
n=0
while read -r line
do
    data[n]="$line"
    echo "Parameter $n: $line"
    ((n++))
done < parameters_in.txt

#downloading file
wget "${data[0]}"
#checking download outcome
if [ $? -eq 0 ]; then
    echo "Download: OK"
else
    echo "Download: FAIL"
fi

#declaring the downloaded file name as an enviroment variable
ls -l "${data[1]}"
DATA_FILE_PATH="$(pwd)/${data[1]}"
echo "Enviroment variable 1: $DATA_FILE_PATH"
export DATA_FILE_PATH

#declaring the age intervals file name (read from the external file) as an enviroment variable
ls -l age_plot_intervals.dat
PLOT_INTERVALS_PATH="$(pwd)/${data[2]}"
echo "Enviroment variable 2: $PLOT_INTERVALS_PATH"
export PLOT_INTERVALS_PATH

#running the python program
python "${data[3]}"

