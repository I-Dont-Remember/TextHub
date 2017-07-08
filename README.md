# TextHub

requires gspread, oauth2client, plivo, flask

"Testing with Plivo, it remains to be seen whether it is the service to
	continue with."

* July 8th: Workable state held together with duct tape and hope. Correct
functionality with basic flask server running on an EC2 instance and tunneled
through ngrok.  Logging and error checking have yet to be handled so that any
errors that might appear from use of two APIs will allow graceful continuation
rather than fiery destruction.
