# swagger_client.PaymentIntentsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_intent**](PaymentIntentsApi.md#cancel_intent) | **POST** /v1/intent/{id}/cancel | Cancel an Intent
[**confirm_payment_intent**](PaymentIntentsApi.md#confirm_payment_intent) | **POST** /v1/intent/{id}/confirm | Confirm a Payment Intent
[**create_payment_intent**](PaymentIntentsApi.md#create_payment_intent) | **POST** /v1/intents/payment | Create a Payment Intent
[**get_intent**](PaymentIntentsApi.md#get_intent) | **GET** /v1/intent/{id} | Get an Intent

# **cancel_intent**
> Intent cancel_intent(authorization, id)

Cancel an Intent

Used to cancel an intent that has not yet finalised, i.e. it has an `unconfirmed` status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentIntentsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID for the payment intent.  A string in the format `intent_[0-9a-z]`.

try:
    # Cancel an Intent
    api_response = api_instance.cancel_intent(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentIntentsApi->cancel_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID for the payment intent.  A string in the format &#x60;intent_[0-9a-z]&#x60;. | 

### Return type

[**Intent**](Intent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_payment_intent**
> Confirmation confirm_payment_intent(body, authorization, id)

Confirm a Payment Intent

In certain cases you may be able to confirm a payment intent from your backend system and not require a user to go through a checkout UI process.  Confirming a payment intent from the API requires a `session_id` to be provided which refers to a session from a [Setup Intent](/resources/setup-intents), that has not already expired.  <Note>   You can only confirm `invoice` payment intents via the API. </Note>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentIntentsApi()
body = swagger_client.IdConfirmBody() # IdConfirmBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing intent that needs to be confirmed.  A string in the format: `intent_[0-9a-z]`

try:
    # Confirm a Payment Intent
    api_response = api_instance.confirm_payment_intent(body, authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentIntentsApi->confirm_payment_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdConfirmBody**](IdConfirmBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing intent that needs to be confirmed.  A string in the format: &#x60;intent_[0-9a-z]&#x60; | 

### Return type

[**Confirmation**](Confirmation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_intent**
> DepositIntent create_payment_intent(body, authorization)

Create a Payment Intent

A payment intent describes a participants intention to fund a project account. We currently support 3 different types of Payment Intent:  - A `checkout` Payment Intent is consumed as soon as a Participant   clicks \"Pay Now\" on the Checkout UI. It therefore, can not be re-used. - A `payment_link` Payment Intent is consumed and can be re-used if it does   not include a `from` Participant. - An `invoice` Payment Intent, although still requiring confirmation of a user,   will not take them through a UI driven process. On confirmation of an   invoice Payment Intent, a new invoice will be provisioned.  <div className=\"not-prose\">   <Button href=\"#create-a-payment-intent-attributes\" variant=\"text\" arrow=\"right\">     See the available attributes   </Button> </div>  ### With or without a defined buyer  A buyer can optionally be provided at the creation of an intent. If no buyer is provided, the user confirming the intent will be asked to provide their email address and a new participant will be created in the system.  At a minimum, when a buyer participant is provided, we require just the email address. However, you can also provide a name and an address which will be used in the UI to further personalise the buyer's experience.  ### Include inline fees  Fees can be applied to a payment intent to charge a buyer at successful completion of a checkout.  Fees can also be applied to a settlement to charge a seller at each successful release from a settlement. You can provide both an optional flat fee and an optional percentage fee to charge. The percentage fee must be provided to the __API__ as a fraction, ie. a fee of `1.5%` is provided to the __API__ as `0.015`.  <Note>   Fees are always calculated as: (`total` * `fee_percentage`) + `fee_flat` </Note>  ### Targeting an existing project  At creation, an intent can optionally be targeted at an existing project. This is useful if you wish to provision a project account up front, or if you need to collect more funds in the event of a discrepancy. You can find more information about how projects relate to the rest of the system by referencing our [Projects](/resources/projects) page.  <Note>   You may not need projects for your use-case. However, every checkout   is backed by an under-lying project account. </Note>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentIntentsApi()
body = swagger_client.IntentsPaymentBody() # IntentsPaymentBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create a Payment Intent
    api_response = api_instance.create_payment_intent(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentIntentsApi->create_payment_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntentsPaymentBody**](IntentsPaymentBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**DepositIntent**](DepositIntent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intent**
> Intent get_intent(authorization, id)

Get an Intent

Retrieve an existing intent.  This endpoint is polymorphic and will return any intent type, including both [Payment Intents](/resources/payment-intents) and [Setup Intents](/resources/setup-intents).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentIntentsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing intent.  A string in the format: `intent_[0-9a-z]`

try:
    # Get an Intent
    api_response = api_instance.get_intent(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentIntentsApi->get_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing intent.  A string in the format: &#x60;intent_[0-9a-z]&#x60; | 

### Return type

[**Intent**](Intent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

