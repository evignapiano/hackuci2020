from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client
import api_keys

app = Flask(__name__)

votes = 0
dict_of_info = {"+16197219618": ["Emily", ""], "+18089310909": ["Tyler", ""], "+17145144501": ["Bryant", ""]}
list_of_nums = ["+18089310909"]  # "+16197219618", "+17145144501"] UNCOMMENT LATER
stage = 1
max = 3
sent = False
client = Client(api_keys.TWILIO_ACCOUNT_SID, api_keys.TWILIO_AUTH_TOKEN)

def send_message(stage, num):
    if stage == 1:
        client.messages.create(
                body='Would you like to order pizza?',
                from_='+14344736168',
                to=num
            )
    if stage == 2:
        client.messages.create(
                body='Which pizza?',
                from_='+14344736168',
                to=num
            )
    if stage == 3:
        client.messages.create(
                body='We will not be having pizza tonight :^(',
                from_='+14344736168',
                to=num
            )


def check_if_max(votes, max):
    return votes == max

def check_majority_vote(votes, max):
    if votes/max >= 0.5:
        return True
    return False

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    list_of_nums = ["+18089310909"]  # "+16197219618", "+17145144501"] UNCOMMENT LATER

    global votes
    global sent
    global dict_of_info
    global stage

    msg = request.values.get("Body", None)
    phone_number = request.values.get("From", None)
    resp = MessagingResponse()

    if msg.lower() == "yes" and dict_of_info[phone_number][1] == "":
        resp.message(dict_of_info[phone_number][0] + " has voted yes for pizza!")
        dict_of_info[phone_number][1] = 1 #1 for yes
        votes += 1
    elif msg.lower() == "no" and dict_of_info[phone_number][1] == "":
        resp.message(dict_of_info[phone_number][0] + " has voted no for pizza.")
        dict_of_info[phone_number][1] = 0  #0 for no
        votes += 1
    else:
        resp.message("You have either entered an invalid response or already voted.")

    if check_if_max(votes, max):
        if stage == 2:
            if check_majority_vote(votes, max):
                #use pizza_api_module
            stage = 5
        elif stage == 1:
            if check_majority_vote(votes, max):
                stage += 1
                votes = 0
                sent = False
                dict_of_info = {"+16197219618": ["Emily", ""], "+18089310909": ["Tyler", ""],
                                "+17145144501": ["Bryant", ""]}
                for num in list_of_nums:
                    send_message(2, num)
                sent = True
            else:
                for num in list_of_nums:
                    send_message(3, num)  # stage 3 = No pizza
                    stage = 5
                    sent = True

    return str(resp)


if __name__ == "__main__":
    if sent == False:
        for num in list_of_nums:
            send_message(1, num)
        sent = True
    app.run(port=5000, debug=True)
