# Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample
Python-based hierarchal clustering and visualisation on genetic expression of breast cancer samples. This project aims to display the correlation of ER status of samples to the clustering model. 

Data source: https://doi.org/10.1073/pnas.1732912100

### Data set

Table 2 ([2912table2.xls](2912table2.xls)) and Table 3 ([2912table3.xls](2912table3.xls)) provided in the appendix of the journal listed in the previous hyperlink. Table 2 is a descriptive table of the phenotypes of the 99 samples, where two of the columns show the ER status tested with ligand-binding assays (LBA) and immunohistochemistry (IHC) methods respectively. Table 3 is a 7650 x 99 gene expression matrix consisting the probe elements values for each of the 99 breast tumour samples. First 5500 probe elements out of 7650 are used for this model.

Table 2 and Table 3 are imported as pandas dataframes with dimensions of 2 x 99 and 5500 x 99 respectively using read_excel().

<img width="338" alt="image" src="https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/443f8ae0-5ce3-4055-b704-b46fc5dfe5d1"> <br />

<img width="390" alt="image" src="https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/6f1c403a-e800-442e-b090-f689b2d5321d">

### Data Pre-processing

The data provided in Table 3 is already processed and normalized. To tailor the dataset for the built in clustering functions in SciPy, some small adjustments are made. First, as the clustering fuction is built for numeric data, the NaN values are replaced with the mean value of the specified probe element over all samples. Then, the dataframe of Table 3 is transposed to a 99 x 5500 dataframe, so that each row represents a sample, to match the how python interpret a dataframe.

<img width="321" alt="image" src="https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/e1f4bcf8-c565-4c6b-b7e3-5f1c0c09b609">

### Model Fitting

The hierarchal clustering submodule of SciPy provides various distance models including ‘single’, ‘complete’, 'average', 'centroid', and ‘ward’. These models can be applied by using different method attributes of the linkage() function.

### Visualization

A dendrogram was built in python for each hierarchal clustering model with the dendrogram() function of the hierarchal clustering submodule.

To differentiate the ER status of the samples, the label colours are manipulated with matplotlib to visualize this attribute. A label colour is assigned to each sample with a python dictionary with reference to the following table.

![image](https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/026ad27a-a7d9-4b19-9c3c-a24bb5c23903)

### Results

Method: 'Single'

![single](https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/69ff301b-e11f-4612-9d43-f0d67772cfe6)

Method: 'Complete'

![complete](https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/8955943d-8dab-4375-975b-86e38801580a)

Method: 'Average'

![average](https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/52a463f5-00bc-4743-b008-5c39a40c4a1b)

Method: 'Centroid'

![centroid](https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/a8d2969e-0427-4278-860e-086df59a962b)

Method: 'Ward'

![ward](https://github.com/elisuu/Hierarchal-Clustering-Model-on-Genetic-Expression-of-Breast-Cancer-Sample/assets/128802324/c2b3ef97-a100-4848-9557-f46cdd3389dc)







