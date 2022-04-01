# RabbitMQ Python Publisher Client Docker Container Example 

This is a simple example to show how to use [pika](https://pika.readthedocs.io/en/stable/) to publish messages to RabbitMQ.

### *Prerequisite* 
- Docker 

### How to run the example
Open a terminal at the repo root directory, and run command `docker-compose up`. You will the logs coming in terminal. 
To check the RabbitMQ dashboard, go to the broswer `http://localhost:15672/` with `user: guest` and `password: guest`.
To turn down the servers, simply run `docker-compose down`.