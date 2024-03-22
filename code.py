# Libraries
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

#Import ER status table
er = pd.read_excel(r'2912table2.xls', sheet_name='Table 7 Relapses', index_col = 0, skiprows = 2, nrows = 99, usecols = "A, N:O")
print(er)

#Data set
#import gene expression table
df = pd.read_excel(r'2912table3.xls', sheet_name='7650_ROW_FINAL_DATA_LOGS', skiprows = 2, nrows = 5500, usecols = "G:DA", na_values = "     NA")
print(df)

#Replace NaN of gene expression table with mean value of the probe element over all samples and transpose the table
dfNorm = df.T.fillna(df.T.mean())
print(dfNorm)

#Calculate the distance between each sample
method = 'ward' #change to 'single', 'complete', 'average', 'centroid' for different hierarchal clustering algorithms
Z = linkage(dfNorm, method)
 
#Plot dendrogram
dendrogram(Z, leaf_rotation=90, leaf_font_size=6, labels=dfNorm.index)

#Preset label colors for visualization based on ER status
label_colors = {}
for x in range(99):
    label_colors[er.index[x]] = 'g' if (er.iat[x,0] and er.iat[x,1]) else 'm' if (er.iat[x,0]) else 'c' if (er.iat[x,1]) else 'r'

print(label_colors)

#Change label colors
ax = plt.gca()
xlbls = ax.get_xmajorticklabels()
for x in xlbls:
        x.set_color(label_colors[x.get_text()])

# Show the graph
plt.show()
