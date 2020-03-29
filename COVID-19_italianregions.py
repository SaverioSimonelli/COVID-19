import pandas as pan
import matplotlib.pyplot as plt
from xml.etree import ElementTree as ET

def config(confile):
    tree = ET.parse(confile)
    #print(tree)
    root = tree.getroot()
    
    itaregions = []
    params = []
    level = root.findall("./italianregions/region")
    for child in level:
        if child.tag == "region": itaregions.append(child.text)
    level = root.findall("./params/param")
    for child in level:
        if child.tag == "param": params.append(child.text)    
    return itaregions, params

def plot_italianregions(infile, regions, dois,legends,fname):
    datarow=pan.DataFrame()
    data = pan.DataFrame()
    date = pan.DataFrame()
    diffs=[]
    df = pan.read_json(infile)
    for region in regions:
        
        regcol = df.loc[lambda df: df["denominazione_regione"]==region]
        date=regcol["data"]

        data = regcol[dois]
        print(data.columns)
        
        plt.plot(date,data)
        
        plt.xticks(rotation=210)
       
    plt.savefig(fname)
    plt.legend(legends, loc = "upper left")
    plt.title(regions)
    plt.show()
    return 

confile= "covid-19_ItalianRegions.xml"
infile = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json"

fname = "covid-19_ItalianRegions.png"


regions, dois = config(confile)

legends=[]
for region in regions:
    for doi in dois:
        legend = region+"__"+doi
        legends.append(legend)

plot_italianregions(infile, regions, dois,legends,fname)


