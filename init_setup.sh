echo [$(date)]: START

echo [$(date)]: Create an env with python 3.8 version

conda create --prefix ./env python==3.8 -y

echo [$(date)]: activating the env

source activate ./env

pip install -r requirements.txt

echo [$(date)]: END