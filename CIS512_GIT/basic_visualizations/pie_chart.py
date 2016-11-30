import matplotlib.pyplot as plt
import numpy as np

def piechart(sizes,labels,colors,explode):

       # The slices will be ordered and plotted counter-clockwise.
       #labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
       #sizes= [a,b,c,d]
       #sizes = [15, 30, 45, 10]
       #colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
       #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

       plt.pie(sizes, explode=explode, labels=labels, colors=colors,
               autopct='%1.1f%%', shadow=True, startangle=90)
       # Set aspect ratio to be equal so that pie is drawn as a circle.
       plt.axis('equal')

       fig = plt.figure()
       ax = fig.gca()


       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(0, 0), frame=True)
       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(0, 1), frame=True)
       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(0, 2), frame=True)
       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(1, 0), frame=True)
       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(1, 1), frame=True)
       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(1, 2), frame=True)
       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(2, 0), frame=True)
       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(2, 1), frame=True)
       ax.pie(np.random.random(5), explode=explode, labels=labels, colors=colors,
              autopct='%1.1f%%', shadow=True, startangle=90,
              radius=0.25, center=(2, 2), frame=True)

       ax.set_xticks([0, 1, 2])
       ax.set_yticks([0, 1, 2])
       ax.set_xticklabels(["Sunny", "Cloudy", "Thundering"])
       ax.set_yticklabels(["Dry", "Rainy", "Snowy"])
       ax.set_xlim((-0.5, 2.5))
       ax.set_ylim((-0.5, 2.5))

       # Set aspect ratio to be equal so that pie is drawn as a circle.
       ax.set_aspect('equal')

       plt.show()