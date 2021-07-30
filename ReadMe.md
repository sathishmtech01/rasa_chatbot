### ChatBot using RASA framework

###Rasa:
    The Rasa Stack is a set of open source machine learning tools for developers to create contextual AI assistants and chatbots:
        
        - Core = a chatbot framework with machine learning-based dialogue management
        - NLU = a library for natural language understanding with intent classification and entity extraction
    
    NLU and Core are independent. You can use NLU without Core, and vice versa. We recommend using both

###Installation

    csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ create conda env rasa_chatbot
    csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ source activate rasa_chatbot
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ pip install -U rasa_core 
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ pip install rasa_nlu[tensorflow]
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ pip install -r requirements.txt
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ sudo ~/anaconda/envs/rasa_chatbot/bin/python -m spacy download en
 
 
 
###
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ make train-nlu
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ make train-core
    
    Terminal 1
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$make action-server
    
    Terminal 2
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$make start-rasanlu
    
    Terminal 3
    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$make start-rasacore


### Rasa UI
#### Pgsql
    Download: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
    csk@csk-ai-revolution:~$ cd Downloads/
    csk@csk-ai-revolution:~/Downloads$ chmod +x postgresql-10.8-1-linux-x64.run 
    csk@csk-ai-revolution:~/Downloads$ ./postgresql-10.8-1-linux-x64.run 
    csk@csk-ai-revolution:~/Downloads$ sudo ./postgresql-10.8-1-linux-x64.run 
    
    Download Rasaui db:

    (rasa_chatbot) csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ wget https://raw.githubusercontent.com/paschmann/rasa-ui/master/resources/database/dbcreate.sql
    
    In the sql file
    Replace 
    :postgres_user
    
    To
    postgres
    
    Start Postgres:
    
        
    csk@csk-ai-revolution:~/Downloads$ sudo -i -u postgres
    $ psql
    Password: 
    psql.bin (10.8)
    Type "help" for help.
    
    Cannot read termcap database;
    using dumb terminal settings.
    postgres=# create database rasaui;
    CREATE DATABASE
    postgres=# \c rasaui
    You are now connected to database "rasaui" as user "postgres".
    rasaui=# \i /home/csk/PycharmProjects/rasa_chatbot/dbcreate.sql
    rasaui=# \q
    could not save history to file "/opt/PostgreSQL/10/.psql_history": Permission denied
    $ exit
    
    
    Nodejs Installation:
    Download: https://nodejs.org/en/
    csk@csk-ai-revolution:/opt$ sudo cp /home/csk/Downloads/node-v10.15.3-linux-x64.tar.xz /opt/
    csk@csk-ai-revolution:/opt$sudo tar -xvf node-v10.15.3-linux-x64.tar.xz
    
    Step 3: Set the environment variable by editing ~/.profile. Write the following command:

    nano ~/.profile
    Add the following lines to the end:
    
    # NodeJS
    export NODEJS_HOME=/opt/node-v10.15.3-linux-x64/bin
    export PATH=$NODEJS_HOME:$PATH
    Step 4: Refresh profile by:
    
    . ~/.profile
    Also add the lines inside ~/.bashrc file to the end of the file by:
    
    nano ~/.bashrc
    Step 5: Test Node installation via:
    
    node -v
    It should show the following output on terminal:
    
    v10.1.0
    Also check the npm version via:
    
    npm version
    It should show the following output on terminal:
    

    csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ git clone https://github.com/paschmann/rasaui.git
    Cloning into 'rasaui'...
    remote: Enumerating objects: 16, done.
    remote: Counting objects: 100% (16/16), done.
    remote: Compressing objects: 100% (13/13), done.
    remote: Total 2252 (delta 1), reused 15 (delta 1), pack-reused 2236
    Receiving objects: 100% (2252/2252), 2.71 MiB | 206.00 KiB/s, done.
    Resolving deltas: 100% (1195/1195), done.
    Checking connectivity... done.
    csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot$ cd rasaui
    csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot/rasaui$ npm install
    csk@csk-ai-revolution:~/PycharmProjects/rasa_chatbot/rasaui$ npm start
    
    > RasaUI@2.5.1 start /home/csk/PycharmProjects/rasa_chatbot/rasaui
    > node server/server.js
    
    
    2019-05-18 14:25:17.261|rasa-ui|info|Rasa UI Server: http://localhost:5001;
    2019-05-18 14:25:17.264|rasa-ui|info|;
    2019-05-18 14:25:17.316|rasa-ui|info|;
    2019-05-18 14:25:17.316|rasa-ui|info|Rasa NLU Connected;
    2019-05-18 14:25:17.316|rasa-ui|info|Using connection string from: package.json;
    2019-05-18 14:25:17.316|rasa-ui|info|Rasa NLU Server: http://localhost:5003;
    2019-05-18 14:25:17.316|rasa-ui|info|;
    2019-05-18 14:25:17.320|rasa-ui|info|;
    2019-05-18 14:25:17.320|rasa-ui|info|Rasa Core Connected;
    2019-05-18 14:25:17.320|rasa-ui|info|Using connection string from: package.json;
    2019-05-18 14:25:17.320|rasa-ui|info|Rasa Core Server: http://localhost:5004;
    2019-05-18 14:25:17.320|rasa-ui|info|;
    2019-05-18 14:25:17.353|rasa-ui|info|;
    2019-05-18 14:25:17.353|rasa-ui|info|Postgres DB Connected;
    2019-05-18 14:25:17.353|rasa-ui|info|Using connection string from: package.json;
    2019-05-18 14:25:17.353|rasa-ui|info|Postgres Server: 127.0.0.1:5432;
    2019-05-18 14:25:17.354|rasa-ui|info|Database:rasaui;
    2019-05-18 14:25:17.354|rasa-ui|info|Schema:rasa_ui;
    2019-05-18 14:25:17.354|rasa-ui|info|;
    2019-05-18 14:25:48.010|rasa-ui|info|POST /api/v2/auth;
    2019-05-18 14:25:48.010|rasa-ui|info|No Token, but got an Auth request. Allowing it;
    2019-05-18 14:25:48.012|rasa-ui|info|Authenticate User;
    2019-05-18 14:25:48.012|rasa-ui|info|Information didnt match or not provided.;
    2019-05-18 14:25:52.371|rasa-ui|info|POST /api/v2/auth;
    2019-05-18 14:25:52.371|rasa-ui|info|No Token, but got an Auth request. Allowing it;
    2019-05-18 14:25:52.372|rasa-ui|info|Authenticate User;
    2019-05-18 14:25:52.372|rasa-ui|info|Information didnt match or not provided.;
    2019-05-18 14:26:00.709|rasa-ui|info|POST /api/v2/auth;
    2019-05-18 14:26:00.709|rasa-ui|info|No Token, but got an Auth request. Allowing it;
