import numpy as np
import matplotlib.pyplot as plt
import string 
import matplotlib.patches as mpatches

f = open('data.csv','r')
i = 0

X1 = []
X2 = []
Y1 = []
Y2 = []

for lines in f:
	if i!= 0:
		line = string.split(lines,',')
		if line[5].strip() == 'Male':
			if line[4] == 'Literate Population by age 15 - 24 ':
				X1.append(line[6])
				i+=1
			else:
				X2.append(line[6])
				i+=1
		else:
			if line[4] == 'Literate Population by age 15 - 24 ':
				temp = '-'+line[6]
				Y1.append(temp)
				i+=1
			else:
				temp = '-'+line[6]
				Y2.append(temp)
				i+=1
	else:
		i+=1


total =  (i-1)/4

totals = np.arange(total)

plt.bar(totals, X2, facecolor='#9999ff', edgecolor='white')
plt.bar(totals, X1, facecolor='#4444ff', edgecolor='white')
plt.bar(totals, Y2, facecolor='#ff9999', edgecolor='white')
plt.bar(totals, Y1, facecolor='#ff4444', edgecolor='white')

c9999ff = mpatches.Patch(color='#9999ff', label='Total number of male population')
c4444ff = mpatches.Patch(color='#4444ff', label='Literate male population')
cff9999 = mpatches.Patch(color='#ff9999', label='Total number of female population')
cff4444 = mpatches.Patch(color='#ff4444', label='Literate female population')
plt.legend(handles=[cff4444,cff9999,c9999ff,c4444ff])

plt.ylabel('Number of people')
plt.xlabel('Districts')

plt.show()
