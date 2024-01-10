import numpy as np
import matplotlib.axis as axis
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cmasher as cmr
import math
import os


#opening data file using the enviroment viriable
data_filename = os.environ.get('DATA_FILE_PATH')
print(data_filename)
data = np.loadtxt(str(data_filename), usecols=(1,2,4,8,12),unpack=True)
m_h = data[0]
m_ini = data[1]
m_ass = data[2]
b_y = data[3]
age_p = data[4]

#opening the age intervals file using the enviroment variable
data_filename2 = os.environ.get('PLOT_INTERVALS_PATH')
data2 = np.loadtxt(str(data_filename2),unpack=True)
age_inf = data2[0]
age_sup = data2[1]


######################################################################

#regrouping the stars in age intervarls and defining a color array by slicing a default palette with the cmasher package
n = len(age_inf)
intervals = [0*i for i in range(n)]
colors = [0*i for i in range(n)]
palette = cmr.take_cmap_colors('turbo', n)
for i in range(n):
	intervals[i] = np.where((age_p > age_inf[i] ) & (age_p <= age_sup[i]))
	colors[i] = mcolors.rgb2hex(palette[i])

#plottong the hr diagram 
plt.figure('H-R_diagram', figsize=(14,11))
plt.title('H-R diagram')
plt.xlabel('b-y')
plt.ylabel('$M_V$')

for i in range(n):
	plt.scatter(b_y[intervals[i]],m_ass[intervals[i]],c=colors[i],s=3.0, label= str(age_inf[i]) + ' - ' + str(age_sup[i]) + ' Gyr')
	
plt.legend(markerscale=4.0,fontsize='9')
plt.xlim(min(b_y)-0.02,max(b_y)+0.2)
plt.ylim(max(m_ass)+0.2,min(m_ass)-0.2)


######################################################################

plt.figure('Metallicity_histograms', figsize=(10,7))
plt.title('Metallicity histograms')
plt.xlabel('[M/H]')
plt.ylabel('N')

#defining the three star populations and choosing a color for each population
pop = [np.where(age_p < 1.0), np.where((age_p > 1.0 ) & (age_p <= 5.0)), np.where(age_p > 5.0)]
labels_pop = ['0.0-1.0 Gyr', '1.0-5.0 Gyr', '5.0-14.0 Gyr']
colors = ['deepskyblue', 'orange', 'red']

#plotting the metallicity histograms using 20 bins
for i in range(3):
	plt.hist(m_h[pop[i]],bins=20,color=colors[i],histtype='step',linewidth=1.5,label= labels_pop[i])
	plt.axvline(x = np.mean(m_h[pop[i]]),color=colors[i],linestyle='--',label='Mean = ' + str(round(np.mean(m_h[pop[i]]),2)),alpha=0.5)
	plt.axvline(x = np.median(m_h[pop[i]]),color=colors[i],linestyle='dotted',label='Median = '+ str(round(np.median(m_h[pop[i]]),2)) ,alpha=0.5)
	
plt.legend(markerscale=4.0,fontsize='15')
plt.xlim(min(m_h),max(m_h))


##############################################################

plt.figure('Metallicity_Inital_Mass', figsize=(10,7))
plt.title('Metallicity - Initial Mass')
plt.xlabel('Initial Mass')
plt.ylabel('[M/H]')

#plotting the mass-metallicity graph with lower transparency on the most populated groups of stars
transp = [0.2,0.2,1.0]
for i in range(3):
	plt.scatter(m_ini[pop[i]],m_h[pop[i]],c=colors[i], s=5.0, label= labels_pop[i], alpha=transp[i])	

plt.legend(markerscale=4.0,fontsize='15')
plt.xlim(min(m_ini),max(m_ini))
plt.ylim(min(m_h),max(m_h))

plt.show()


	
