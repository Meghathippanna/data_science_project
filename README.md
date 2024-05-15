# This is my end to end project

Create a folder "data_science_project" and open it in VS Code

 Initalize git by 
```

git init

```

 create a README.md file and note the steps

 Commit changes to the github-- either by source control or by entering code at Terminal- git bash

 Create a .gitignore file in git and add basic template for python

 Create a LICENSE file in git and add any template LICENSE
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

Research.ipynb - proceeding with data ingestion and basic analysis of features of the data

