from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    
    msg = request.values.get("Body").lower().strip()
    resp = MessagingResponse()
    
    print(msg)

    if msg == "pizza":
        resp.message("Ordering a pizza now...")

        
    # Add a message
    # resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)