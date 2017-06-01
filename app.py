import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '359191636:AAEv6zHkkb38dbrNBmhSAUFboizkVdXhemM'
WEBHOOK_URL = 'https://1e693045.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
				'start',
				'organic',
				'inorganic',
				'OL',
				'OH',
				'L',
				'H',
				'CL',
				'CLML',
				'ML',
				'CH',
				'MH'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'start',
            'conditions': 'is_going_to_start'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'inorganic',
            'conditions': 'is_going_to_inorganic'
        },
        {
            'trigger': 'advance',
            'source': 'inorganic',
            'dest': 'L',
            'conditions': 'is_going_to_L'
        },
        {
            'trigger': 'advance',
            'source': 'L',
            'dest': 'CL',
            'conditions': 'is_going_to_CL'
        },
        {
            'trigger': 'advance',
            'source': 'L',
            'dest': 'CLML',
            'conditions': 'is_going_to_CLML'
        },
        {
            'trigger': 'advance',
            'source': 'L',
            'dest': 'ML',
            'conditions': 'is_going_to_ML'
        },
        {
            'trigger': 'advance',
            'source': 'inorganic',
            'dest': 'H',
            'conditions': 'is_going_to_H'
        },
        {
            'trigger': 'advance',
            'source': 'H',
            'dest': 'CH',
            'conditions': 'is_going_to_CH'
        },
        {
            'trigger': 'advance',
            'source': 'H',
            'dest': 'MH',
            'conditions': 'is_going_to_MH'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'organic',
            'conditions': 'is_going_to_organic'
        },
        {
            'trigger': 'advance',
            'source': 'organic',
            'dest': 'OL',
            'conditions': 'is_going_to_OL'
        },
        {
            'trigger': 'advance',
            'source': 'organic',
            'dest': 'OH',
            'conditions': 'is_going_to_OH'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
								'OL',
								'OH',
								'CL',
								'CLML',
								'ML',
								'CH',
								'MH'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
