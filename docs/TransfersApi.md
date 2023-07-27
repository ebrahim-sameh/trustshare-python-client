# swagger_client.TransfersApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transfers**](TransfersApi.md#create_transfers) | **POST** /v1/transfers | Create Transfers
[**get_transfer**](TransfersApi.md#get_transfer) | **GET** /v1/transfer/{id} | Get a Transfer

# **create_transfers**
> TransferResult create_transfers(body, authorization)

Create Transfers

Used to create internal transfers between project accounts.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransfersApi()
body = swagger_client.V1TransfersBody() # V1TransfersBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create Transfers
    api_response = api_instance.create_transfers(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->create_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1TransfersBody**](V1TransfersBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**TransferResult**](TransferResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer**
> Transfer get_transfer(authorization, id)

Get a Transfer

Retrieve an existing transfer.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransfersApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing transfer.  A string in the format: `transfer_[0-9a-z]`

try:
    # Get a Transfer
    api_response = api_instance.get_transfer(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->get_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing transfer.  A string in the format: &#x60;transfer_[0-9a-z]&#x60; | 

### Return type

[**Transfer**](Transfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

