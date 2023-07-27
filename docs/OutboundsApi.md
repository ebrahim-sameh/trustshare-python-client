# swagger_client.OutboundsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_outbound**](OutboundsApi.md#cancel_outbound) | **POST** /v1/outbound/{id}/cancel | Cancel an Outbound
[**create_refunds**](OutboundsApi.md#create_refunds) | **POST** /v1/outbounds/refunds | Create Refunds
[**create_releases**](OutboundsApi.md#create_releases) | **POST** /v1/outbounds/releases | Create Releases
[**get_outbound**](OutboundsApi.md#get_outbound) | **GET** /v1/outbound/{id} | Get an Outbound

# **cancel_outbound**
> Outbound cancel_outbound(authorization, id)

Cancel an Outbound

Used to cancel an outbound where execution has not started yet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutboundsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID for the outbound.  A string in the format `outbound_[0-9a-z]`.

try:
    # Cancel an Outbound
    api_response = api_instance.cancel_outbound(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundsApi->cancel_outbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID for the outbound.  A string in the format &#x60;outbound_[0-9a-z]&#x60;. | 

### Return type

[**Outbound**](Outbound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_refunds**
> OutboundResult create_refunds(body, authorization)

Create Refunds

Used to create refunds against settlements.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutboundsApi()
body = swagger_client.OutboundsRefundsBody() # OutboundsRefundsBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create Refunds
    api_response = api_instance.create_refunds(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundsApi->create_refunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OutboundsRefundsBody**](OutboundsRefundsBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**OutboundResult**](OutboundResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_releases**
> OutboundResult create_releases(body, authorization)

Create Releases

Used to create releases from projects and settlements.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutboundsApi()
body = swagger_client.OutboundsReleasesBody() # OutboundsReleasesBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create Releases
    api_response = api_instance.create_releases(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundsApi->create_releases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OutboundsReleasesBody**](OutboundsReleasesBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**OutboundResult**](OutboundResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound**
> Outbound get_outbound(authorization, id)

Get an Outbound

Retrieve an outbound release or refund payment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutboundsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing outbound.  A string in the format: `outbound_[0-9a-z]`

try:
    # Get an Outbound
    api_response = api_instance.get_outbound(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutboundsApi->get_outbound: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing outbound.  A string in the format: &#x60;outbound_[0-9a-z]&#x60; | 

### Return type

[**Outbound**](Outbound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

