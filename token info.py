import requests
from datetime import datetime

def Main():
    print('''
 _____     _              _     ___     
|_   _|___| |_ ___ ___   | |___|  _|___ 
  | | | . | '_| -_|   |  | |   |  _| . |
  |_| |___|_|_|___|_|_|  |_|_|_|_| |___|
       
''')
    token = input('Token: ')

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    req = requests.get('https://discordapp.com/api/v8/users/@me', headers=headers)
    req_json = req.json()
    #Name stuff
    uid = req_json['id']
    name = req_json['username']
    discriminator = req_json['discriminator']
    full_name = f'{name}#{discriminator}'
    #Contact info + Creation date
    phone_number = req_json['phone']
    email = req_json['email']
    creation_date = datetime.utcfromtimestamp(((int(uid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    #Big avatar stuff
    avatid = req_json['avatar']
    avaturl = f'https://cdn.discordapp.com/avatars/{uid}/{avatid}.png'
    #2Fa/Mfa
    mfa = req_json['mfa_enabled']
    if mfa == True:
        mfa = 'Yes'
    else:
        mfa = 'No'
    
    print(f'''
            Name: {full_name}
            Avatar URL: {avaturl}
            Creation date: {creation_date}
            Phone number: {phone_number}
            E-Mail: {email}
            2FA/MFA Enabled: {mfa}
            ''')

if __name__ == '__main__':
    Main()