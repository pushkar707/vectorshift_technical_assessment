# slack.py

import os
from backend.redis_client import add_key_value_redis
from fastapi import Request
from dotenv import load_dotenv
load_dotenv()
import json
import secrets

CLIENT_ID = os.environ.get('HUBSPOT_CLIENT_ID')
CLIENT_SECRET = os.environ.get('HUBSPOT_CLIENT_SECRET')
REDIRECT_URI = f'{os.environ.get('ROOT_DOMAIN')}/integrations/airtable/oauth2callback'
authorization_url = f'https://app.hubspot.com/oauth/authorize?client_id={CLIENT_ID}&scope=contacts%20automation&redirect_uri={REDIRECT_URI}'


async def authorize_hubspot(user_id, org_id):
    state_data = {
        'state': secrets.token_urlsafe(32),
        'user_id': user_id,
        'org_id': org_id
    }
    encoded_state = json.dumps(state_data)
    await add_key_value_redis(f'hubspot_state:{org_id}:{user_id}', encoded_state, expire=600)
    return f'{authorization_url}&state={encoded_state}'


async def oauth2callback_hubspot(request: Request):
    # TODO
    pass


async def get_hubspot_credentials(user_id, org_id):
    # TODO
    pass


async def create_integration_item_metadata_object(response_json):
    # TODO
    pass


async def get_items_hubspot(credentials):
    # TODO
    pass
