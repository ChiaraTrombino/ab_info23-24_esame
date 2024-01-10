This work was tested in an Anaconda enviroment using Python 3.6.13 (install the cmasher package!)


INSTALLATION:
All the files have to be saved in the same folder.
You have to give "py_run.sh" the execution permission (chmod +x). 
The application "py_run.sh" has to be run with the following command (the command is written as a comment inside the script, it can also be copied from there):

./py_run.sh cartella_esame py_files_and_variables.sh star_pops.py age_plot_intervals.dat parameters_in.txt

"py_run.sh" creates the folder "cartella_esame" (or any other name) in the current path, copies all the other files given as arguments inside the new folder and run "py_files_and_variables.sh".

"py_files_and_variables.sh" reads the lines from "parameters_in.txt". 
It downloads a file from the github link (line 1) inside the new folder. 
It creates a first enviroment variable for the path of the downloaded file (file name in line 2) and a second enviroment variable for the path of "age_plot_intervals.dat" (line 3). 
Then it runs the program "star_pops.py" (line 4) which uses the two enviroment variables. 


PYTHON PROGRAM:
"star_pops.py" uses the data from "Nemo_6670.dat" (the downloaded file) to produce three graphics:
1) an HR diagram using the age intervals from "age_plot_intervals.dat", the age intervals colors are picked from a default palette using the cmasher package;
2) metallicity histograms for three star population defined in the program and indipendent from "age_plot_intervals.dat". It also shows the mean and median for each histogram;
3) mass-metallicity graph for the previous three populations, the points of th more populated ones are shown with lower opacity.
