# Climate Emergency Hackathon Example Site

This site was developed as part of the OFGEM organised climate energy hackathon in January 2020. 

Our group was developing an MVP for a trading exchange to facilitate heating network connections and trades.

<br>

### Activating the Virtual Environment
Go to the top directory inside the repository and run
```
.\env\Scripts\activate
```
or you may need to instead run 
```
source env/Scripts/activate
```
Either way, get that Virtual Environment running. You will be rewarded by your terminal saying `(env)` at the far left.

### Install requirements
Now that you are running in a python virtual environment, you should install the project requirements.
```
pip install -r requirements.txt
```


### Launching the Site
```
python main.py
```

### Publish the site
#### Creating static version with Flask-Freeze
```
python freeze.py

# To check the static build:
python -m http.server --directory build
# view at localhost:8000
```
