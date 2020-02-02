from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
account_sid = 'ACd5474723664cffd4cd919d5d9019facc'
auth_token = '16433b3f464b5e2654fb25ed4226fe9c'

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    
    msg = request.values.get("Body", None)
    print(request.form["From"])
    resp = MessagingResponse()
    
    print(msg)

    if msg == "pizza":
        resp.message("Ordering a pizza now...")
        
    # Add a message
    # resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)