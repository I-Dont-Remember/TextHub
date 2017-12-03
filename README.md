# sms2sheets

**Structure**  
```text
sms2sheets/  
  app\  
    config.py  
    main.py  
    sheets.py    

  .gitignore  
  Dockerfile  
  client.json   
  requirements.txt  
  README   
  venv\  
    <virtual environment files>  
```
*Testing with Plivo, it remains to be seen whether it is the service to 
continue with.*
--Switched to Twilio

* July 8th: Workable state held together with duct tape and hope. Correct
functionality with basic flask server running on an EC2 instance and tunneled
through ngrok.  Logging and error checking have yet to be handled so that any
errors that might appear from use of two APIs will allow graceful continuation
rather than fiery destruction.

* July 17th: Had small spurts of time to add to this over the past week.
Refactored some sections for ease of expanding on this concept later, added early
stages of logging and config stuff, and got Docker working.
