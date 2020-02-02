from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import send_message


app = Flask(__name__)
account_sid = 'ACd5474723664cffd4cd919d5d9019facc'
auth_token = '16433b3f464b5e2654fb25ed4226fe9c'

dict_of_info = {"Emily": "+16197219618", "Tyler": "+18089310909", "Bryant": "+17145144501"}

class Pizza_Poll:
    def __init__(self, max):
        self.votes = 0
        self.dict_of_info = {"+16197219618" : ["Emily", 0], "+18089310909": ["Tyler", 0], "+17145144501": ["Bryant", 0]}
        self.stage = 1
        self.max = max
        self.sent = False

    def check_if_max(self):
        return self.votes == self.max

    def return_stage(self):
        return self.stage

    def return_sent(self):
        return self.sent


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply(current_poll):
    """Respond to incoming calls with a simple text message."""

    msg = request.values.get("Body", None)
    phone_number = request.form["From"]
    resp = MessagingResponse()

    if msg.lower() == "yes" and current_poll.dict_of_info[phone_number][0][1] != 1:
        resp.message(current_poll.dict_of_info[phone_number][0][0] + " has voted yes for pizza!")
        current_poll.dict_of_info[phone_number][0][1] += 1
        current_poll.votes += 1
    elif msg.lower() == "no" and current_poll.dict_of_info[phone_number][0][1] != 1:
        resp.message(current_poll.dict_of_info[phone_number][0][0] + " has voted no for pizza.")
        current_poll.dict_of_info[phone_number][0][1] += 1
        current_poll.votes += 1
    else:
        resp.message("You have either entered an invalid response or already voted.")

    return str(resp)

if __name__ == "__main__":
    new_poll = Pizza_Poll(3)
    new_send = send_message.Send()
    app.run(debug=True)
    while True:
        if new_poll.return_sent() == False:
            new_send.send_to_all(new_poll.return_stage())
            new_poll.sent = True
        if new_poll.check_if_max() == True:
            if new_poll.stage == 1:
                new_poll.votes = 0
                new_poll.stage += 1
                new_poll.sent = False
            else:
                pass
                #call pizza api