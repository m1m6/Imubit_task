# Tech stack used
  - [Python](http://flask.pocoo.org/) Flask microframework: to build apis.
  - [Mysql](https://www.mysql.com/) database: host records of users.
  - [Docker](https://www.docker.com/): contanarize the application.
  - [Docker-compose](https://docs.docker.com/compose/): run multiple containers, app container, mysql container.
  - [SocketIO](https://flask-socketio.readthedocs.io/en/latest/): sends data to clients at real time.
  - HTML and JQuery: handle client side view.

# Installation
  - Clone this repo.
  - Open terminal and navigate to project root Dir
    ``` 
    USER@ubuntu:~$ cd ~/monitor-linux-login
    ```
  - Under utilites folder, there will be two files (shell and service).
  - Copy ```after_login_trigger.sh``` to ```/etc/profile.d``` folder
    - ```cp after_login_trigger.sh /etc/profile.d```
  - Open ```docker-flask-server.service``` file with any editor, and update the path for ```docker-compose.yml``` file according to the file location in your machine.
      - ExecStart=/usr/bin/docker-compose start -f ```/home/mahmoud/PycharmProjects/monitor-linux-login/compose/docker-compose.yml```
      - ExecStop=/usr/bin/docker-compose stop -f ```/home/mahmoud/PycharmProjects/monitor-linux-login/compose/docker-compose.yml```
    - Copy ```docker-flask-server.service``` to ```/etc/systemd/system/```
      - ```cp docker-flask-server.service /etc/systemd/system/```
    - Enable the service at startup
      - ``` sudo systemctl enable docker-flask-server.service```


### Running the application
There's two options to run the application (on both cases the app will run on port ```5000```):

##### 1- Through docker
In this case just restart your machine, and before login don't forget to bring your coffee cup 😂.
Enter your credentials, and hit login, and your user should be added to the DB, navigate to localhost:5000, it should be listed there.

Or execute the ```file docker-env.sh``` which will run the application inside docker env
  - ```chmod +x docker-env.sh```
  - ```./docker-env.sh```

![users list](https://i.imgur.com/GpyIeiV.jpg)


##### 2- Through IDE
  - Go to file ```db_model.py``` and update the ```host``` to be ```localhost```, also update db credentials ```user``` and ```passwrod``` if they are required to be changed.
  - Using workbench/ phpmyadmin, or any DBMS, create a new database ```users_flask```, and apply the content of the file
  ```monitor-linux-login/mysql/mysqlInit.sql``` to that DB.
  - On the root DIR, execute ```python login_watcher.py```

### How to use
As i mentioned before, just after restarting your machine and login, your user should be listed. And will be considerd as LOCAL login. For the second options by using ssh, just open your terminal and write down the connection command
```ssh USER@localhost -p 22```
and the result should be directly displayed.
![users list](https://i.imgur.com/gIH8YBa.gif)



