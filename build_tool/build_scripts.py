import json
import asyncio
import os

import requests

def run_project_build(build_data):
    # NJOGUSH_BASE_URL = settings.NJOGUSH_BASE_URL_CUSTOM_DOMAIN
    # NJOGUSH_SOCKET_URL = settings.NJOGUSH_SOCKET_URL_CUSTOM_DOMAIN
    # NJOGUSH_TOKEN = settings.NJOGUSH_TOKEN_CUSTOM_DOMAIN

    NJOGUSH_BASE_URL = "http://127.0.0.1:6564"
    NJOGUSH_SOCKET_URL = "ws://127.0.0.1:6564"
    NJOGUSH_TOKEN = build_data["token"]

    project_id = build_data["project_id"]

    # + https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers
    headers_njogush = {
        # 'user-agent': 'my-app/0.0.1',
        'Authorization': f'Token {NJOGUSH_TOKEN}'
    }

    # STEP 4: Run project
    data = {'action': 'run', 'command_arguments': build_data.get('command_arguments', '')}
    r = requests.patch(f'{NJOGUSH_BASE_URL}/api/projects/{project_id}/', data=data, headers=headers_njogush)
    r.raise_for_status()
    build_session = r.json()

    build_session_id = build_session['id']
    asyncio.run(client(f'{NJOGUSH_SOCKET_URL}/ws/build/{build_session_id}/', NJOGUSH_BASE_URL))


# TODO https://websockets.readthedocs.io/en/stable/faq/client.html#how-do-i-stop-a-client-that-is-processing-messages-in-a-loop
import json
import asyncio
import signal
import websockets

async def client(uri, origin):
    # uri = "ws://localhost:8765"
    async with websockets.connect(uri, origin=origin) as websocket:
        # Close the connection when receiving SIGTERM.
        # loop = asyncio.get_running_loop()
        # loop.add_signal_handler(
        #     signal.SIGTERM, loop.create_task, await websocket.close())

        # a Python object (dict):
        x = {
            "message": "run",
        }
        message = json.dumps(x)
        await websocket.send(message)
        # message = websocket.recv()
        # print(f"Received: {message}")

        # Process messages received on the connection.
        async for message in websocket:
            # some JSON:
            x =  '{ "name":"John", "age":30, "city":"New York"}'

            message = json.loads(message)
            # print(message)
            message_signal = message.get('signal')
            if message_signal == 'stop' or message_signal == 'finish':
                await websocket.close()