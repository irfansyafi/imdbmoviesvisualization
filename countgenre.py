'''
Series is a one-dimensional array of data with an associated array of labels, called an index.
For example, using the count_genres output:

Drama   656
Comedy  220
Crime   181
Action  179
...     ...


DataFrame is a two-dimensional table of data with rows and columns. To easily understand DataFrame, it is similar
to spreadsheet or SQL table where it have columns and rows

can call openCSV.head() to see the sample of the DataFrame

'''

import pandas as pd
from matplotlib import pyplot as plt

openCSV = pd.read_csv(r"yourpathhere\.csv")

openCSV.head() #to show a sample of the DataFrame

#the column 'Genre' contains multiple genre.
count_genres = openCSV['Genre'].str.split(expand=True).stack() #helps to split the genre into new column and assign to count_genres Series
count_genres = count_genres.value_counts() #help count the occurence of the genre

print(count_genres) #to print the genre and the counts

rangeGross = [0,100,200,300,400,500,1000] #range that wants to be specified for the bins parameter in pd.cut() function
labelrange = ['0-100','100-200','200-300','300-400','400-500','More than 500'] #labels for x-axis when showing the graph


count_grossrange = pd.cut(openCSV['grossMillions($)'],bins=rangeGross).value_counts() #counts the ranged of the grossMillions

print(count_grossrange)


#custom the bar color by specifying in a list
colorbar = ['red','blue','purple']

count_genres.plot(kind='bar',color = colorbar)   #using bar chart

#customizing the title,x-label and y-label for count_genres Series
plt.title('Genre Counts')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show() #it is a good practice to always use plt.show() to show the graph ***it still can show without the plt.show()

count_grossrange.plot(kind='bar')
#customizing the title, x-label and y-label
plt.title("Range of Gross in Millions for Top 1000 IMDb")
plt.xlabel('Range')
plt.ylabel('Gross in Millions')

#customizing the xtick, if not it specify here it will automatically show the rangeGross. Example : (0,100) (100,200) etc
plt.xticks(range(len(labelrange)),labelrange)

#to add value at the top of each bar
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])
        
addlabels(labelrange,count_grossrange)

plt.show()


