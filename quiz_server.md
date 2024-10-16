# Creating a quiz server for SEELab3

Objective: I need a way for teachers to conduct real time quizzes
in the classroom where they use the desktop app to send MCQ questions which are
relayed via the server to the android apps of the students.

Tools: fastapi, redis, gunicorn, socketio


## The server

Built with fastapi and redis for scalability, it hosts socketio, and allows folks to create quiz rooms
with passwords. students can then join these rooms.

testing : python3 socket_server.py
deploy: gunicorn -w 4 -k uvicorn.workers.UvicornWorker socket_server:app

## Clients

### Teacher

a testing script connects and creates a room. when the server says room has been created, it starts sending questions to that room's members

### Student

A testing script connects and listens for questions
a shell script is used to spin up multiple students

`for i in {1..20}; do python3 test_student.py & done`

for killing all

`kill $(jobs -p)`

## Screenshots

Deploying
![](/images/quiz/deploy.png)

Running
![](/images/quiz/run.png)


