from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC0d28b66e975fc52bdbf15e1a277b2862"
# Your Auth Token from twilio.com/console
auth_token  = "f8273a4565968eb5f63cadfa2a18a03b"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+19192658621",
    from_="+19195253401",
    body="Hello from Python!")

print(message.sid)
