# swagger_client.SettlementsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_settlement**](SettlementsApi.md#cancel_settlement) | **POST** /v1/settlement/{id}/cancel | Cancel a Settlement
[**get_settlement**](SettlementsApi.md#get_settlement) | **GET** /v1/settlement/{id} | Get a Settlement

# **cancel_settlement**
> Settlement cancel_settlement(authorization, id)

Cancel a Settlement

Used to cancel a settlement that has not yet finalised, i.e. it has a `settling` status.  A cancellable settlement may already have a reconciled balance, in which case, after being cancelled, the balance can be used in all the normal ways: release/refund/transfer. This situation can occur when the buyer is using manual bank transfers to pay.  <Note>   The primary use for cancelling a settlement is to stop any funds being reconciled to it in the future. </Note>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettlementsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID for the settlement.  A string in the format `settlement_[0-9a-z]`.

try:
    # Cancel a Settlement
    api_response = api_instance.cancel_settlement(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementsApi->cancel_settlement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID for the settlement.  A string in the format &#x60;settlement_[0-9a-z]&#x60;. | 

### Return type

[**Settlement**](Settlement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settlement**
> Settlement get_settlement(authorization, id)

Get a Settlement

Retrieve an existing settlement.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettlementsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing settlement.  A string in the format: `settlement_[0-9a-z]`

try:
    # Get a Settlement
    api_response = api_instance.get_settlement(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettlementsApi->get_settlement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing settlement.  A string in the format: &#x60;settlement_[0-9a-z]&#x60; | 

### Return type

[**Settlement**](Settlement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

