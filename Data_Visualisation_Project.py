#These are the libraries imported into the to project. Matplotlib allows for graphs and charts to be created
#Numpy allows for arrays to be created and used within the matplot charts.
#Tkinter allows for a GUI to be developed, allowing for interactivity.
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

# This section sets up the Tkinter home screen allowing the user to select a graph.
# Here, the blank canvas, title and size of the pop-up are initilised
root =Tk()
root.title("Data Visualisation")
root.geometry("500x100")

# This function plots the graph for the overall data from all 3 months.
def graph():

    csfont = {'fontname': 'Krungthep'} #this allows for the font to be changed and will be called throughout the code
    plt.figure(facecolor='steelblue', figsize=(12, 8)) #this changes the colour of the face of the visulisation and the dimensions of the graph

    ax = plt.axes()
    ax.set_facecolor("honeydew") #this allows for the background colour to be changed

    # Here, the data for the Y axis and the X axis are plotted. The final line in this sequence plots the scatter graph
    # and alters the colour.
    y = np.array([562765, 488395,473741,501569,509870,584386, 560698, 474356, 550805,563952])
    x = np.array(["E. Midlands","London","N. East","N. West","Scotland","S. East","S. West","Wales","W. Midlands","Yorkshire"])
    plt.scatter(x, y, color = 'indigo')


    y = np.array([495696, 434820, 433509 , 429681,457336,517349,479186,411124,471446,492751])
    x = np.array(["E. Midlands","London","N. East","N. West","Scotland","S. East","S. West","Wales","W. Midlands","Yorkshire"])
    plt.scatter(x, y, color = 'lightseagreen')

    y = np.array([519340,443630,456460,454430,463830,523023,480397,424904,494227,504300])
    x = np.array(["E. Midlands","London","N. East","N. West","Scotland","S. East","S. West","Wales","W. Midlands","Yorkshire"])
    plt.scatter(x, y, color = 'hotpink')

    # This section allows for the legend to be plotted and the location to be set.
    # Also, here the labels for each axis are named and the font variable is called from earlier in the code.
    #Finally, the title of the chart is named.
    plt.legend(["September", "October", "November"], loc ="lower right")
    plt.xlabel("Locations",**csfont)
    plt.ylabel("Fuel Cost (£)",**csfont)
    plt.title("Average Fuel Prices for Locations",**csfont, fontweight = 'bold')

    # This shows the graph on the screen.
    plt.show()


#This function plots the data for just September.
def graph_sep():

    plt.figure(facecolor='steelblue', figsize=(12, 8)) #This sets the background colour and the size of the chart.

    #This sets the background colour on the face of the chart.
    ax = plt.axes()
    ax.set_facecolor("honeydew")

    # Here, the data for the Y axis and the X axis are plotted. The final line in this sequence plots the scatter graph
    # and alters the colour.
    y = np.array([562765, 488395, 473741, 501569, 509870, 584386, 560698, 474356, 550805, 563952])
    x = np.array(
        ["E. Midlands", "London", "N. East", "N. West", "Scotland", "S. East", "S. West", "Wales", "W. Midlands",
         "Yorkshire"])
    plt.scatter(x, y, color='indigo')

    #Here the labels for the axes are named and the font changed. The title is also given here.
    csfont = {'fontname': 'Krungthep'}
    plt.xlabel("Locations", **csfont)
    plt.ylabel("Fuel Cost (£)", **csfont)
    plt.title("September Average Fuel Prices", **csfont, fontweight='bold')

    # This shows the graph on the screen.
    plt.show()

#This function plots the data for just October.
def graph_oct():

    plt.figure(facecolor='steelblue', figsize=(12, 8))#This sets the background colour and the size of the chart.

    # This sets the background colour on the face of the chart.
    ax = plt.axes()
    ax.set_facecolor("honeydew")

    # Here, the data for the Y axis and the X axis are plotted. The final line in this sequence plots the scatter graph
    # and alters the colour.
    y = np.array([495696, 434820, 433509, 429681, 457336, 517349, 479186, 411124, 471446, 492751])
    x = np.array(
        ["E. Midlands", "London", "N. East", "N. West", "Scotland", "S. East", "S. West", "Wales", "W. Midlands",
         "Yorkshire"])
    plt.scatter(x, y, color='lightseagreen')

    # Here the labels for the axes are named and the font changed. The title is also given here.
    csfont = {'fontname': 'Krungthep'}
    plt.xlabel("Locations", **csfont)
    plt.ylabel("Fuel Cost (£)", **csfont)
    plt.title("October Average Fuel Prices", **csfont, fontweight='bold')

    # This shows the graph on the screen.
    plt.show()

#This function plots the data for just November.
def graph_nov():

    plt.figure(facecolor='steelblue', figsize=(12, 8)) #This sets the background colour and the size of the chart.

    # This sets the background colour on the face of the chart.
    ax = plt.axes()
    ax.set_facecolor("honeydew")

    # Here, the data for the Y axis and the X axis are plotted. The final line in this sequence plots the scatter graph
    # and alters the colour.
    y = np.array([519340, 443630, 456460, 454430, 463830, 523023, 480397, 424904, 494227, 504300])
    x = np.array(
        ["E. Midlands", "London", "N. East", "N. West", "Scotland", "S. East", "S. West", "Wales", "W. Midlands",
         "Yorkshire"])
    plt.scatter(x, y, color='hotpink')

    # Here the labels for the axes are named and the font changed. The title is also given here.
    csfont = {'fontname': 'Krungthep'}
    plt.xlabel("Locations", **csfont)
    plt.ylabel("Fuel Cost (£)", **csfont)
    plt.title("November Average Fuel Prices", **csfont, fontweight='bold')

    #This shows the scatter plot to the user
    plt.show()


#Here are the seperate buttons the user can press to access the different charts. Namely, the overall 3 months, and the individual months.

overall = Button(root, text = "Overall", command=graph)
overall.pack()

sep = Button(root, text = "September", command=graph_sep)
sep.pack()

oct = Button(root, text = "October", command=graph_oct)
oct.pack()

nov = Button(root, text = "November", command=graph_nov)
nov.pack()

root.mainloop()
