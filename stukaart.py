import keyboard, requests, json, re

CLIENT_ID=''
CLIENT_SECRET=''

TOKEN_URL="https://idp.kuleuven.be/auth/realms/kuleuven/protocol/openid-connect/token"
API_ENDPOINT = "https://account.kuleuven.be/api/v1/idverification"
PATTERN = re.compile(r".*([0-9a-fA-F]{14};[0-9]{10}).*")

def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]

def listen_for_scanner():
    scannerInput = ""
    while PATTERN.search(scannerInput) is None:
        scannerInput = ""
        recorded = keyboard.record(until='enter',suppress=True)[:-1]
        print("Scanner input received")
        for key in recorded:
            if key.event_type == 'down' and key.name != 'shift' and key.name != 'maj':
                # temp fix since `§` key is unknown
                scannerInput += key.name if key.name != 'unknown' else '6'
        if(scannerInput == ''): keyboard.write('\n')
        if(scannerInput == 'esc'): exit()
        if PATTERN.search(scannerInput) is None:
            print("Invalid input, waiting for retry...")
    return PATTERN.search(scannerInput).group(1).split(";")

def get_username_from_scanner_details(details):
    (serial, cardId) = details
    req = requests.request('POST', API_ENDPOINT, json={
        "serialNr": serial,
        "cardAppId": cardId
    }, headers={
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Authorization" : "Bearer " + AUTH_TOKEN,
    })

    profile = json.loads(req.text)
    return profile.get("userName")

def write_username(length, username):
    for i in range(0,length):
        keyboard.write("\b")
    keyboard.write(username)
    keyboard.write("\n")

def main():
    print("Press esc+enter twice in order to exit the program")
    global AUTH_TOKEN
    print("Getting access token...")
    AUTH_TOKEN = get_access_token(TOKEN_URL, CLIENT_ID, CLIENT_SECRET)
    print("Access token received")
    keyboard.add_abbreviation('enter', '\n')
    while True:
        print("Waiting for scanner input...")
        details = listen_for_scanner()
        length = len(details[1]) + len(details[0]) + 1
        print("Correct input, retrieving username...")
        username = get_username_from_scanner_details(details)
        write_username(length, username)

if __name__ == "__main__":
    main()
