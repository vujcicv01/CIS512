from CIS512_GIT.basic_visualizations.pie_chart import piechart

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs', 'Pogs'
sizes = [15,30,30,10,15]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'orange']
explode = (0, 0.1, 0, 0,0.2)  # only "explode" the 2nd slice (i.e. 'Hogs')

piechart(sizes=sizes,labels=labels,explode=explode,colors=colors)
