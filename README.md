# Tweet_cloud App
This is flask app, built on python3 which uses Twitter Api's to fetch tweets of the hashtag which the user sends via GET request and present WordCloud of all the tweets. 

# Installation:
1. Clone the project
    ```python3
    git clone https://github.com/yashasingh/Tweet_cloud.git 
    ```
2. Create a virtualenv
    ```python3
    virtualenv -p python3 venv
    ```
3. Activate the virtualenv
    ```python3
    source venv/bin/activate
    ```
4. Now install all the dependencies in requirements.txt using the following command :
    ```python3
    pip intsall -r requirements.txt
    ```
5. Fill your API key values obtained from Twiiter developer account in the ApiKeyValues.py file, which requires yours access_token, access_secret, consumer_key and consumer_secret key.

# Running the project:
This command will run a temprorary local flask server at 127.0.0.1:5000
```python
python3 app.py
```
# Result
Now u access my wordcloud Api using url using 127.0.0.1:5000/wordcloud/query="your_query"
The result obtained would be as follows :  
query = despacito
![alt text](https://raw.githubusercontent.com/yashasingh/Tweet_cloud/master/assets/despacito.png)

query = enrique
![alt text](https://raw.githubusercontent.com/yashasingh/Tweet_cloud/master/assets/enrique.png)

query = sachin
![alt text](https://raw.githubusercontent.com/yashasingh/Tweet_cloud/master/assets/sachin.png)

query = virat
![alt text](https://raw.githubusercontent.com/yashasingh/Tweet_cloud/master/assets/virat.png) 



