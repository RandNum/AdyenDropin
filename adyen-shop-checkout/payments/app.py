import json
import requests

def lambda_handler(event, context):
    url = "https://checkout-test.adyen.com/v64/paymentMethods"
  
    paymentMethod = {'type': 'scheme', 'encryptedCardNumber': 'adyenjs_0_1_18$k7s65M5V0KdPxTErhBIPoMPI8HlC..', 'encryptedExpiryMonth': 'adyenjs_0_1_18$p2OZxW2XmwAA8C1Avxm3G9UB6e4..', 
                    'encryptedExpiryYear': 'adyenjs_0_1_18$CkCOLYZsdqpxGjrALWHj3QoGHqe+..', 'encryptedSecurityCode': 'adyenjs_0_1_18$XUyMJyHebrra/TpSda9fha978+..', 'holderName': 'S. Hopper'}
    
    
    payload = {
          "amount": [{ "currency":"EUR", "value":1000 }],
          "reference":"23409817234",
          "paymentMethod": paymentMethod,
          "returnUrl":"https://your-company.com/checkout?shopperOrder=12xy",
          "merchantAccount":"AdyenRecruitmentCOM"
          }

    print(json.dumps(payload))

    headers = {
      'content-type': 'application/json',
      'x-API-key': 'AQEyhmfxLI3MaBFLw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFitRvbe4N1XqH1eHaH2AksaEQwV1bDb7kfNy1WIxIIkxgBw==-y3qzswmlmALhxaVPNjYf74bqPotG12HroatrKA066yE=-W+t7NF;s4}%=kUSD'
    }
    response = requests.post(url, headers=headers, data = payload)
    #print(response.json())
    
    
    returnObject = {
        'statusCode': 200,
        'body': response.json()
    }
    print(json.dumps(returnObject))

    return returnObject
