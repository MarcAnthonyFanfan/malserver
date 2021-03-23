# Setting up Web Application Security Attack Infrastructure using Flask and Python with Juice Shop
The following guide assumes that you have Git and Docker installed already, as installation methods on different operating systems can vary greatly.

1. Clone this repository locally to your machine.
```
git clone <repo_url>
```

2. Change directories to the cloned repo folder.
```
cd malserver
```

3. Build the docker image and run a container using that image.
```
docker build -t malserver .
docker run -it --rm -v $(pwd):/malserver -p 8080:8080 malserver
```

4. Open your browser to http://localhost:8080/ and you should see the following response:
```
Did not receieve username and cookie params
```

5. Modify the url to include username and cookie params. For example, we will use username=Test1 and cookie=Test2, but these can be anything: http://localhost:8080/?username=Test1&cookie=Test2

6. Press enter after the params have been added to the url. You should the following reponse:
```
Received username=Test1 cookie=Test2
```

7. Check your project folder for a new file called **cookies.log** - this file will contain a log of all cookies that malserver receives.
Every time you run the server, it also logs the time at which the session was started. For example:
```
New Session Started: 2021-03-23 17:54:07.273424
Captured username=Test1 cookie=Test2
```