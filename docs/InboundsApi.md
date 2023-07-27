# swagger_client.InboundsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inbound**](InboundsApi.md#get_inbound) | **GET** /v1/inbound/{id} | Get an Inbound

# **get_inbound**
> Inbound get_inbound(authorization, id)

Get an Inbound

Retrieve an inbound payment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InboundsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing inbound.  A string in the format: `inbound_[0-9a-z]`

try:
    # Get an Inbound
    api_response = api_instance.get_inbound(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundsApi->get_inbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing inbound.  A string in the format: &#x60;inbound_[0-9a-z]&#x60; | 

### Return type

[**Inbound**](Inbound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

