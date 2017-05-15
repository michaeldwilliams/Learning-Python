from twilio.rest import TwilioRestClient
import send_text_config

config = send_text_config

client = TwilioRestClient(config.account_sid, config.auth_token)

message = client.messages.create(
    to= config.to_number,
    from_= config.from_number,
    body="Hello from Python!")

print(message.sid)
