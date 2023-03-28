from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


load_dotenv()

app = Flask(__name__)
client = Client()

load_dotenv()


# To create the message

def create(message):
    data = client.messages.create(
                              from_='whatsapp:Enter your demo twilio number',
                              body=message,
                              to='whatsapp:Enter the where you want to send message.'
                          )
    print("Data", data)
    print("SID Data", data.sid)
    return data.sid


@app.route('/create/message', methods=['POST'])
def create_message():
    return create("Hello")

# To respond the message

# def respond(message):
#     response = MessagingResponse()
#     response.message(message)
#     return str(response)


# @app.route('/respond/message', methods=['POST'])
# def reply():
#     return respond(f'Thank you for your message! A member of our team will be in touch with you soon.')


@app.route("/respond/message", methods=['GET', 'POST'])
def reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)