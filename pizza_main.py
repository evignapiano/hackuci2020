from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client
import api_keys
import pizza_api_module

app = Flask(__name__)

votes = 0
total_responses = 0
dict_of_info = {"+16197219618": ["Emily", ""], "+18089310909": ["Tyler", ""], "+17145144501": ["Bryant", ""]}
list_of_nums = ["+18089310909", "+16197219618", "+17145144501"]
stage = 1
max = 3
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
                body='Which pizza? Choose between Brooklyn or Thin Wisconsin.',
                from_='+14344736168',
                to=num
            )
    if stage == 3:
        client.messages.create(
                body='We will not be having pizza tonight :^(',
                from_='+14344736168',
                to=num
            )
    if stage == 4:
        client.messages.create(
                body='Your order has been placed for Brooklyn!',
                from_='+14344736168',
                to=num
            )
    if stage == 5:
        client.messages.create(
                body='Your order has been placed for Thin Wisconsin!',
                from_='+14344736168',
                to=num
            )


def check_if_max(total_responses, max):
    return total_responses == max

def check_majority_vote(votes, max):
    if votes/max >= 0.5:
        return True
    return False

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    list_of_nums = ["+18089310909", "+16197219618", "+17145144501"]

    global votes
    global sent
    global dict_of_info
    global stage
    global total_responses

    msg = request.values.get("Body", None)
    phone_number = request.values.get("From", None)
    resp = MessagingResponse()

    if msg.lower() == "yes" and dict_of_info[phone_number][1] == "" and stage == 1:
        resp.message(dict_of_info[phone_number][0] + " has voted yes for pizza!")
        dict_of_info[phone_number][1] = 1 #1 for yes
        votes += 1
        total_responses += 1
    elif msg.lower() == "no" and dict_of_info[phone_number][1] == "" and stage == 1:
        resp.message(dict_of_info[phone_number][0] + " has voted no for pizza.")
        dict_of_info[phone_number][1] = 0  #0 for no
        total_responses += 1
    elif msg.lower() == "brooklyn" and dict_of_info[phone_number][1] == "" and stage == 2:
        resp.message(dict_of_info[phone_number][0] + " has chosen Brooklyn pizza")
        dict_of_info[phone_number][1] = "brooklyn"
        votes += 1
        total_responses += 1
    elif msg.lower() == "thin wisconsin" and dict_of_info[phone_number][1] == "" and stage == 2:
        resp.message(dict_of_info[phone_number][0] + " has chosen Thin Wisconsin pizza")
        dict_of_info[phone_number][1] = "thin wisconsin"
        total_responses += 1
    else:
        resp.message("You have either entered an invalid response or already voted.")

    if check_if_max(total_responses, max):
        if stage == 2:
            if check_majority_vote(votes, max):
                for num in list_of_nums:
                    pizza_api_module.order_pizza(dict_of_info[num][0], "Appleseed", "someone@uci.edu", num, '2272 Michelson Dr, Irvine, CA, 92612', "brooklyn")
                    send_message(4, num)
            else:
                for num in list_of_nums:
                    pizza_api_module.order_pizza(dict_of_info[num][0], "Appleseed", "someone@uci.edu", num, '2272 Michelson Dr, Irvine, CA, 92612', "thin wisconsin")
                    send_message(5, num)
            stage = 6
        elif stage == 1:
            if check_majority_vote(votes, max):
                stage += 1
                votes = 0
                total_responses = 0
                dict_of_info = {"+16197219618": ["Emily", ""], "+18089310909": ["Tyler", ""],
                                "+17145144501": ["Bryant", ""]}
                for num in list_of_nums:
                    send_message(2, num)
            else:
                for num in list_of_nums:
                    send_message(3, num)  # stage 3 = No pizza
                stage = 6

    return str(resp)


if __name__ == "__main__":
    for num in list_of_nums:
        send_message(1, num)
    app.run(port=5000, debug=True)
