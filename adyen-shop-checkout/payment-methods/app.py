import json
import requests

def lambda_handler(event, context):

    url = "https://checkout-test.adyen.com/v64/paymentMethods"
    
    payload = "{\n  \"merchantAccount\": \"AdyenRecruitmentCOM\",\n  \"countryCode\": \"NL\",\n  \"amount\": {\n    \"currency\": \"EUR\",\n    \"value\": 1000\n  },\n  \"channel\": \"Web\",\n  \"shopperLocale\": \"nl-NL\"\n}"
    headers = {
      'content-type': 'application/json',
      'x-API-key': 'AQEyhmfxLI3MaBFLw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFitRvbe4N1XqH1eHaH2AksaEQwV1bDb7kfNy1WIxIIkxgBw==-y3qzswmlmALhxaVPNjYf74bqPotG12HroatrKA066yE=-W+t7NF;s4}%=kUSD'
    }
    response = requests.post(url, headers=headers, data = payload)
    print(response.json())
    

    
    returnObject = {
        'statusCode': 200,
        'body': response.json()
    }
    print(json.dumps(returnObject))

    return returnObject
    