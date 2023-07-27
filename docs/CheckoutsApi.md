# swagger_client.CheckoutsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_checkout**](CheckoutsApi.md#get_checkout) | **GET** /v1/checkout/{id} | Get a Checkout

# **get_checkout**
> Checkout get_checkout(authorization, id)

Get a Checkout

Retrieve an existing checkout.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing checkout.  A string in the format: `checkout_[0-9a-z]`

try:
    # Get a Checkout
    api_response = api_instance.get_checkout(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutsApi->get_checkout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing checkout.  A string in the format: &#x60;checkout_[0-9a-z]&#x60; | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

