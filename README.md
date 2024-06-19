# This is my end to end project
Create a folder "data_science_project" and open it in VS Code
Initalize git by 

```
git init
```

Create a README.md file and note the steps
Create a .gitignore file in git and add basic template for python
Commit changes to the github-- either by source control or by entering code at Terminal- git bash

```
git add .
git commit -m "This is my first commit"
```

Create a LICENSE file in git and add any template LICENSE. Eg: MIT License
License required for production, to provide permission and limitations
Git pull the license to your VSCode 

```
git pull
```

Create a init_setup.sh ( shell script works only for linux terminal. since git bash is linux terminal. i have written in shell script)
Write codes to create a env and activate the env
run the shell script

```
bash init_setup.sh
```

create a template.py file and import os and path and create a list of files namely
1. src/package- DiamondPricePrediction folder  
    --> components-__init__.py, data_ingestion.py, data_transformation.py, model_trainer.py
    --> pipelines- __init__.py, training_pipeline.py, prediction_pipeline.py 
    --> utils- __init__.py
    --> __init__.py
    --> logger.py
    --> exception.py
2. notebooks    
    --> data - .gitkeep
    --> research.ipynb
3. requirements.txt
4. setup.py
5. init_setup.sh (already created)
6. .github/workflows
    -->.gitkeep

Run template.py to get all the files mentioned in the list

```
python template.py
```

To install DiamondPricePrediction , write setup codes in setup.py and run

```
python setup.py install
```

Other ways to install DiamondPricePrediction is to add "-e ." in the requirements.txt and run

```
pip install -r requirements.txt
```

Day-2
Research.ipynb - proceeding with data ingestion and basic analysis of features of the data

Import required libraries and read the csv file 
Understand the data and the features. Determine dependent and independent features
separate categorical and numerical columns
Describe to determine mean, mode, for categorical and numerical columsn
Visualize the data- distribution and heatmap 
Proceed with ordinal encoding
Feature scaling, check for null values
Create pipeline of steps of Feature Engineering
Split train and test dataset
Fit transform for train data and 
Transform for test data


Proceed with Regression as the dependent feature value is continous
Get the LinearRegression, Lasso, Ridge, ElasticNet model's r2 value

Day3
Update files data_ingestion.py; data_transformation.py; model_trainer.py with def and pass
Write code to create a  Log file in Logger.py
Write code to creat a custom exception in Exception.py

```
from src.DimondPricePrediction.logger import logging
```


ther end
