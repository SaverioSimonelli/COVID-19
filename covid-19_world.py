import pandas as pan
import matplotlib.pyplot as plt
from xml.etree import ElementTree as ET

def config(confile):
    tree = ET.parse(confile)
    
    root = tree.getroot()
    countries = []
    wparams = []
    itaregions = []
    irparams = []
    
    level = root.findall("./countries/country")
    
    for child in level:
        if child.tag == "country": countries.append(child.text)
    level = root.findall("./wparams/wparam")
    for child in level:
        if child.tag == "wparam": wparams.append(child.text)  
    return countries, wparams
    
    
def plot_world(infile, countries, columnnames, fname, legends):
    colname = "Country"
    datarow=pan.DataFrame()
    data = pan.DataFrame()
    date = pan.DataFrame()
    #diffs=[]
    df = pan.read_csv(infile)
    
    for country in countries:
        datarow = df.loc[lambda df: df[colname]== country]
        data = datarow[columnnames]
        
        plt.plot(datarow["Date"],data)
        
        plt.legend(legends)
        plt.title(columnnames)
        ax = plt.gca()
        
        plt.xticks(rotation=25)
        
        for label in ax.get_xaxis().get_ticklabels()[::2]:
            label.set_visible(False)
    plt.savefig(fname)
    plt.show()
    print (data)
    
    return


confile="covid-19_world.cfg"
countries,columnnames = config(confile)

url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
fname = "covid-19_world.png"



legends=[]
for country in countries:
    for columnname in columnnames:
        legend = country+"__"+columnname
        legends.append(legend)

plot_world(url, countries, columnnames, fname, legends)