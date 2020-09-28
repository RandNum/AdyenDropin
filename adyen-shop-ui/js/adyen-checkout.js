

// const initiateAyden = async () => {
//     const paymentMethodsResponse = await fetch('https://484xjman23.execute-api.eu-central-1.amazonaws.com/prod')
//     const paymentMethodsData = await paymentMethodsResponse.json()
//     console.log(paymentMethodsData.body)
//     console.log(paymentMethodsData.body["paymentMethods"])
//     return paymentMethodsData.body
//     }

// const paymentMethods = initiateAyden();
// console.log(1, paymentMethods)

// const configuration = {
//     paymentMethodsResponse: paymentMethods, // The `/paymentMethods` response from the server.
//     clientKey: "test_CIXAPNBW2JERLEJ6GYYC3WBLVMO2HIZ3", // Web Drop-in versions before 3.10.1 use originKey instead of clientKey.
//     locale: "en-US",
//     environment: "test",
//     onSubmit: (state, dropin) => {
//         // Your function calling your server to make the `/payments` request
//         makePayment(state.data)
//           .then(response => {
//             if (response.action) {
//               // Drop-in handles the action object from the /payments response
//               dropin.handleAction(response.action);
//             } else {
//               // Your function to show the final result to the shopper
//               showFinalResult(response);
//             }
//           })
//           .catch(error => {
//             throw Error(error);
//           });
//       },
//     onAdditionalDetails: (state, dropin) => {
//       // Your function calling your server to make a `/payments/details` request
//       makeDetailsCall(state.data)
//         .then(response => {
//           if (response.action) {
//             // Drop-in handles the action object from the /payments response
//             dropin.handleAction(response.action);
//           } else {
//             // Your function to show the final result to the shopper
//             showFinalResult(response);
//           }
//         })
//         .catch(error => {
//           throw Error(error);
//         });
//     },
//     paymentMethodsConfiguration: {
//       card: { // Example optional configuration for Cards
//         hasHolderName: true,
//         holderNameRequired: true,
//         enableStoreDetails: true,
//         hideCVC: false, // Change this to true to hide the CVC field for stored cards
//         name: 'Credit or debit card'
//       }
//     }
// };

// const checkout = new AdyenCheckout(configuration);
// console.log(2, checkout)
// const dropin = checkout.create('dropin').mount('#dropin-container');

const fetchPromise = fetch("https://pdv2gzx94a.execute-api.eu-central-1.amazonaws.com/Prod/payment-methods")
fetchPromise
.then(res => {return res.json()})
.then(response => {
    console.log("Payment Methods:", response)
    
    const configuration = {
        paymentMethodsResponse: response, // The `/paymentMethods` response from the server.
        clientKey: "test_CIXAPNBW2JERLEJ6GYYC3WBLVMO2HIZ3", // Web Drop-in versions before 3.10.1 use originKey instead of clientKey.
        locale: "en-US",
        environment: "test",
        onSubmit: (state, dropin) => {
            // Your function calling your server to make the `/payments` request
            console.log(3, state.data.paymentMethod)
            const data = state.data.paymentMethod;
            console.log(4, JSON.stringify(data))
                fetch('https://pdv2gzx94a.execute-api.eu-central-1.amazonaws.com/Prod/payments', {
                method: 'POST', 
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
                })
                .then(response => response.json())
                .then(data => {
                console.log('Success:', data);
                })
                .catch((error) => {
                console.error('Error:', error);
                });
            makePayment(state.data)
              .then(response => {
                if (response.action) {
                  // Drop-in handles the action object from the /payments response
                  dropin.handleAction(response.action);
                } else {
                  // Your function to show the final result to the shopper
                  showFinalResult(response);
                }
              })
              .catch(error => {
                throw Error(error);
              });
          },
        onAdditionalDetails: (state, dropin) => {
          // Your function calling your server to make a `/payments/details` request
          makeDetailsCall(state.data)
            .then(response => {
              if (response.action) {
                // Drop-in handles the action object from the /payments response
                dropin.handleAction(response.action);
              } else {
                // Your function to show the final result to the shopper
                showFinalResult(response);
              }
            })
            .catch(error => {
              throw Error(error);
            });
        },
        paymentMethodsConfiguration: {
          card: { // Example optional configuration for Cards
            hasHolderName: true,
            holderNameRequired: true,
            enableStoreDetails: true,
            hideCVC: false, // Change this to true to hide the CVC field for stored cards
            name: 'Credit or debit card'
          }
        }
       };

       const checkout = new AdyenCheckout(configuration);
       console.log(2, checkout)
       const dropin = checkout.create('dropin').mount('#dropin-container');

    //    console.log("end of inner .then config")
});


// console.log("end of custom config js file ")