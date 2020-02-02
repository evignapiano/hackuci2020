from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

class Send:
    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.list_of_nums = ["+16197219618", "+18089310909", "+17145144501"]
        self.client = Client(self.account_sid, self.auth_token)

    def send_to_all(self, stage):
        for num in self.list_of_nums:
            if stage == 1:
                message = self.client.messages \
                        .create(
                             body="Would you like to order pizza?  Reply yes or no.",
                             from_='+14344736168',
                             to=num
                         )
            elif stage == 2:
                message = self.client.messages \
                        .create(
                             body="Reply 1 for pepperoni pizza or 2 for cheese pizza",
                             from_='+14344736168',
                             to=num
                         )
        print(message.sid)
        return str(message)