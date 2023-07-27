# swagger_client.SetupIntentsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_setup_intent**](SetupIntentsApi.md#create_setup_intent) | **POST** /v1/intents/setup | Create a Setup Intent
[**get_intent**](SetupIntentsApi.md#get_intent) | **GET** /v1/intent/{id} | Get an Intent

# **create_setup_intent**
> SetupIntent create_setup_intent(body, authorization)

Create a Setup Intent

A setup intent describes a participants intention to allow you to use one of their payment instruments off-session at a later date.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SetupIntentsApi()
body = swagger_client.IntentsSetupBody() # IntentsSetupBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create a Setup Intent
    api_response = api_instance.create_setup_intent(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupIntentsApi->create_setup_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntentsSetupBody**](IntentsSetupBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**SetupIntent**](SetupIntent.md)

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
api_instance = swagger_client.SetupIntentsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing intent.  A string in the format: `intent_[0-9a-z]`

try:
    # Get an Intent
    api_response = api_instance.get_intent(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupIntentsApi->get_intent: %s\n" % e)
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

