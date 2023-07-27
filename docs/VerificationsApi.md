# swagger_client.VerificationsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_verification**](VerificationsApi.md#create_verification) | **POST** /v1/verifications | Create a Verification
[**get_verification**](VerificationsApi.md#get_verification) | **GET** /v1/verification/{id} | Get a Verification

# **create_verification**
> Verification create_verification(body, authorization)

Create a Verification

A Verification describes the intent to verify a participant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerificationsApi()
body = swagger_client.V1VerificationsBody() # V1VerificationsBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create a Verification
    api_response = api_instance.create_verification(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationsApi->create_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VerificationsBody**](V1VerificationsBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**Verification**](Verification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verification**
> Verification get_verification(authorization, id)

Get a Verification

Retrieve an existing verification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerificationsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing verification.  A string in the format: `verification_[0-9a-z]`

try:
    # Get a Verification
    api_response = api_instance.get_verification(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationsApi->get_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing verification.  A string in the format: &#x60;verification_[0-9a-z]&#x60; | 

### Return type

[**Verification**](Verification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

