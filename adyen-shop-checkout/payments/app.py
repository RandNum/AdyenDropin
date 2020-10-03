import json
import requests
import os   #needed to prnt to logs in aws


def lambda_handler(event, context):
    url = "https://checkout-test.adyen.com/v64/payments"
  
    #paymentMethod = {"type":"scheme","holderName":"J. Smith","encryptedCardNumber":"adyenjs_0_1_25$O1NxNKmI/zw1aDdNvk8Kvw2DuHzRB4vQgbmJ0sM51a2PXwFrzuga2FKi6mgIhqaWU0yHjhaUY8bqKEK++2rNVMFQcjt1S6ULTi3EvDUSM90xjsKM3ZwQIsP38Ku+Pzm5exujk1dw9Vu6L3pOEqlLAnylb8lO8CeNiTDWQ/vgi6R6aWVCuhR3HH2jw6YVXDGsVpHdEBTp79LqmS+Ls5xonlWVK40DlIsLW8o2NVLrXWRfMch8xIymbOCkY/u+N/fdDCzYKiAftSK1foaFV5ozYw7uDcBmfrPS1grW7cm2gvzeSQKDSct525dseDpIzVTluc+iFN8u6/q4E8rEEjpgaA==$LVpnu3kNRWclNnlB3gwD5Yl9cNVI3zJme4aResiJ7ti6dIKrDieVXaMpzO/kLM6DNkzVFRfmYnIss1KqNX5MeuGUoMVs9F8A415Mz64StWZYXCU2ImE8FIIHyxKhVZdZja1/d4LnyaFIdZehLVffd6Q27ZcTLYu5WMUm3kwaDVq7hhdJuZ3UdaD/2kkxg30HLKIq8K97CpCe7tOppuefPw8xokJ7GZP/mK4j/JcQNraHYB44Kp7rJFDrC1FuptKM93v7qfQGaHlVvs9j765A5iQqRm33NgjIiVdfxl12pvQcAnEs0hOCqHQ3noT5nFYu1KZZdUmkEt0OaRN8ybhPqmtmViiyTZkSfDMvAnnS1khsZvlgk4Q8FbIT0jOv2AtpqswK5Y2RgaBovRHmfNY7Nt4UxPmFqShf2xBxYANDyjy/DzzBzDJFJULFBtJwb9fd+EydINzP3OGHoHktX/JpqItsZtaRQQC0TKxh7gVClLFilZr4hE2LgJV2G9myOQ1V4N4uUbIsPExrD5O8snlZbCvlWT3gvy782sqHUV0ZNTqdJL9fuYS/aBLiNzcM7J/42E0VHhWSsqSaet2Eviz0oXP3ELQPSYH3AJwqDeRwk7oxW+qP3pO3mBQNflIe2Y9qk1Q11GF5BvYAbnHuP2GwmcF8AZiR3AzN2/X9lvFmPFKvTmy9D12CT2tU/SEOop3LL1O8CwiNu3BCX/a1YVEmzRbuRPXIGqh4tHhCmjOOseAnR/6oRMHYnhLJ5/a7vxy8","encryptedExpiryMonth":"adyenjs_0_1_25$WMpLxnpyDvF+fP2VQkxwEiG0xGdeoX8/ZrKpFXESBjQvCDk/cZgGIrGIEvUtXMxoh0H7M0kCQFaH1WA749PDaiT+jtQnMS2GNhDOUvLwtE7atQcN00O+tyJlDU0HmrzgfVUfA13TIaxtlhObRrgBNmcqadxj2tsMwGZu9zDLSl9ZBMzyNZ+OqIXnYqv1mTVgTegDW4kpkkRuHV3pTma0ojxT3eu1nVaZ68IelpYnTQAl8dJqvh2bSDrmy5QD5zacMTqzmVh7In/mGToFW+4VuA1hjQ80JNj7ZJqrGAktAOhd2qKr5swjya/g2OsWDuGog/5WO8PQP5AM6K3mbJanhw==$EYP+vUnhasjFQZOdUoPMsLntmHpxd9F37Oqp6SOfgut+6HcgKxVcVmAKE/dF6+MZptwRqvfT2O64NecFC8ByMnLFpFZf8LGlMdT1+lwQYUI1e/K5EEOAbr0jJ/DxG/Q9Fy4AfwlHN36ZHsmeMCuZKyPGeDoTc9toyyKujn/gnn1vdBGc1YxM6O/1r5k1UkerlPpUUfSh5GfO/eRMPq19h5KQuYFdmXr2+rzh4pJSinHvD0z6CuySWEVd4NwX6reGzPItvsYer4gJaA04DhLGvMm6eZnTpIcK09gBBayjUkXCqXskQCbA5YrhTDvOZkMtGUMYj+ucCzXrLYjTSBSFVAezSH8k1JuWDNhsOYNFFak05M5k0l0qMS47xL9FZKceGExJ6sh3i0DhQx9EGi2BXGU2tW4KY9o4PIi5wA2eEeOH6bQ=","encryptedExpiryYear":"adyenjs_0_1_25$FqXggownM5yVxfHfxUVdWUdriM3D8+78D3VBJ7cFdLW71LpKt504brJrBTmimLmUcAkqX8p3h62TZTTOXVGPl9eXCws4JH/T0IcWA3ZyZiClmUkH20Gk09tgZAhn9WIS1RGmmBDSssHja1ulkIZE2JGDClIZ1ZKUrZlHtypeo4bE2OqEmlKHNbzad6zmURaHJI7v3AtS5bv0swEjBWU46rZSovizDF9isWXotsKi2CJQs53vlxJ/3BRv4M4TNHYasnD7PVPtPHY6JNdVaVFLkirnlABvS/1m3lC1yyaUp3f7bXSEK2sLqRCtC381gDYlZR8YSCDYJtzxljhzUzN8zw==$BiRiC1UHFHYV06qpODcBPOPBTbi/a1QfFGoR21qq1G49V9TY6UFXOhPxstOZvvUgOaCE/bguqpmAq69PqRSt0yuM2/AtT4LWsQqB/b2Ygz4GlERrqH+MhJzzc7C83PsLr40QJNLBMmYolWwC63Rg8chIEE4FLiN3p2C93qkDm39dpwzRkn5KXezpMc4iuNME/UUbLTQkXDEzWsM+77xsZG3W4CYfpDFU1Uc5n6dmlE60vZk1YjMdmR4hFzjz/AbDPUwSDDGkQFYp44w25CoeHZ3d5Kox0d+MvfaHixWGsyUv3EnA1+5LfWr1xvZjJETUB37DSlw0ZEUhGGZbyabo6mp4fA7TgM72TyC+A1Cgvx3pdqHqe8ddFDt3C89dWwkS2ne1yBdJlvPFUoDQKgAbdHkr+nVe4uLoVUPduLk1oFqxiIt7","encryptedSecurityCode":"adyenjs_0_1_25$XrA+dscG9FV7lvVF5UHmmRrp4z6M8Izu2ZW99SbzNYi9CK2GpGCtLMfDGNqvgchEPek6HsEZQ2QPIVDdyNCm0xofItyYZ190mgD1IHSBoUd8CLQs6+XZbMwIC/+MLMrh6yUstfVOejGf/2StJShy4h/x0W93WnZPJfExEvH7UYYhnyyTO/D1A/qvjmovyBRR0xj6sZkFafcHN50J6awGpDxea8EZNrB7s5U8uCxvb2UAZm1CQQ5QKCM6HElNAo9c7Fg5O7EbFNA/B/yIK6q6XeKc7m9ZvaMAdnp1iGpi3RieqA+2+j1MJxDPKK8J17yUKPx/1eJ2TlTnrfGnj5RoKw==$pUe83f8fth0q+hAuRRBgBDCzy3mnR7TpWsiO0ThxonzYldJaHbS5jZYx3mcokH4Pjmxl/QarPexXdvA9VDH/8zzt9CerdxodA9KzKjckt/qTDqHEBfRxl2Quz7NjfRJdVit7op31nmLWFzzTQcdWTuCnyc86UW91BUw7Ixv+nw0vCpgopKlpyMTCu5GgO/VuQhKsyn6E6jF0e5hNgtkozHXQZw8ZuoR73MOL0xqcvl9vl9/i9Gz9UmZY/TlOhBAkjWTCyh0AjbnRTI4Fvfvh7rEYVEe9naGjib24kLVrB9vXSejgwATnpVwlwvvZ1NXAwwAm0yeN4YhsHFIOxF6Mzb+QpwAez9cQJJ/3WW7mBKYXTbvToY2n8kuU/dyiDHyt1qyQpBDirlkBVNWpMWJdxx5BNi4QsVosutka885vzN6DimNxBhmjamvY8GdZ0Q==","brand":"amex"}
    #paymentBody = event.get('body', '')
    
    paymentEvent = event

    payload = {
          "amount": { "currency":"EUR", "value":1000 },
          "reference":"23409817234",
          "paymentMethod": paymentEvent,
          "returnUrl":"https://your-company.com/checkout?shopperOrder=12xy",
          "merchantAccount":"AdyenRecruitmentCOM"
          }

    #print(json.dumps(payload))

    headers = {
      'content-type': 'application/json',
      'x-API-key': 'AQEyhmfxLI3MaBFLw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFitRvbe4N1XqH1eHaH2AksaEQwV1bDb7kfNy1WIxIIkxgBw==-y3qzswmlmALhxaVPNjYf74bqPotG12HroatrKA066yE=-W+t7NF;s4}%=kUSD'
    }
    response = requests.post(url, data = json.dumps(payload), headers = headers)
    
    print(response)
    
    returnObject = {
        'statusCode': 200,
        'headers':{'Access-Control-Allow-Origin':'*'},
        'body': response.json()
    }
    #print(json.dumps(returnObject))

    return returnObject
