from twilio.rest import Client
import api_keys

# client = Client(api_keys.TWILIO_ACCOUNT_SID, api_keys.TWILIO_AUTH_TOKEN)
# numbers_to_message = ['+18089310909', '+14158141829', '+15017122661']
# message = client.messages \
#     .create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='+14344736168',
#          to='+18089310909')