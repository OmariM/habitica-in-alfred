import secrets

USER_ID = 'a7e29731-49ab-4a26-956f-ca3ba4cfb580'
CLIENT_HEADER = USER_ID + 'Testing'

auth_dict = {
        "x-api-user": USER_ID,
        "x-api-key": secrets.API_TOKEN,
        "x-client": CLIENT_HEADER
}
