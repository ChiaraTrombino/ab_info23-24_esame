#!/bin/bash

#command to run on terminal:
#./py_run.sh cartella_esame py_files_and_variables.sh star_pops.py age_plot_intervals.dat parameters_in.txt

#input arguments used in the script
new_folder="$1"
py_sh="$2"

#creating a new folder
mkdir "$new_folder"

#excluding the folder parameter from the loop by shifting the parameters positions
shift 1
#coping all the other input arguments into the new folder and giving execution permissions
for n in "$@"
do
	cp "$n" "$new_folder"
	chmod +x "$new_folder/$(basename "$n")"
done

#setting the PYTHONPATH and the PATH to include the new folder
export PYTHONPATH="$PYTHONPATH:$new_folder"
export PATH="$PATH:$new_folder"

#entering the new folder
cd "$new_folder"

#running the bash script
source ./"$py_sh"

