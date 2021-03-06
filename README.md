# Assistant Bot For Admission Counselling
> The Development Repository for basic career guidance and admission counselling Chatbot based on RASA Framework.

## Originally Developed and Maintained By:
>> 1. **[Sakshi Khose](https://github.com/sakshi2399)**
>> 2. **[Rutuja Kitukale](https://github.com/rutujakitukale)**
>> 3. **[Jamaluddin Khan](https://github.com/JKhan01)**

## NOTE
>> The rasa version used for the bot is *2.0* . The version is compatible with python **3.6,3.7 and 3.8**

>> The project as of now is a primitive bot which can respond to FYJC colleges based queries using the data available in csv file generated from scraping the *[Teach Us](https://www.teachuseducation.com/)  website* apart from routine interactions.  


## Setting Up for local manual testing and usage 
1. Create a virtual environment of ***python 3.6 or greater***.
2. Clone the repository.
3. Setting up the dependancies.
```
    pip install -r requirements.txt
```

4. Navigate to the *bot1* directory. Run the command:
```
    rasa train
```

5. Once the model gets trained, you are good to launch the Processes on the system.
> 1. Launch the rasa core server:
```
    rasa run -m models --enable-api
```

> 2. Launch the rasa action server. If you don't want to export the actions directory into path. You can navigate to the *actions* sub-driectory of bot1.:
```
    rasa run actions
```

> 3. Launch the flask server by navigating to the *interface/backend* driectory. Again to skip navigation you can export the path of flask app.:
```
    python routes.py
```

> 4. Launch the frontend on the local python http server. Under *interface* directory, run the followng command:
```
    python -m http.server
```

6. Now open your browser and type the following URL:
```
    http://localhost:8000/frontend/UI.html
```
