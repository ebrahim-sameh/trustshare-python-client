# swagger_client.PaymentInstrumentsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_instrument**](PaymentInstrumentsApi.md#create_payment_instrument) | **POST** /v1/payment-instruments | Create a Payment Instrument
[**get_payment_instrument**](PaymentInstrumentsApi.md#get_payment_instrument) | **GET** /v1/payment-instrument/{id} | Get a Payment Instrument

# **create_payment_instrument**
> PaymentInstrument create_payment_instrument(body, authorization)

Create a Payment Instrument

Used to create payment instruments that users can use to complete checkout.  A `trade_account` type payment instrument can only be created for a business. To successfully create a trade account, we will require a number of fields to be provided on the `business` key of the `owner`.  Required fields: `company_number`, `registered_address`, `phone_number`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentsApi()
body = swagger_client.V1PaymentinstrumentsBody() # V1PaymentinstrumentsBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create a Payment Instrument
    api_response = api_instance.create_payment_instrument(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentsApi->create_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PaymentinstrumentsBody**](V1PaymentinstrumentsBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**PaymentInstrument**](PaymentInstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_instrument**
> PaymentInstrument get_payment_instrument(authorization, id)

Get a Payment Instrument

Retrieve an existing payment instrument.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentInstrumentsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing payment instrument.  A string in the format: `payment_instrument_[0-9a-z]`

try:
    # Get a Payment Instrument
    api_response = api_instance.get_payment_instrument(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInstrumentsApi->get_payment_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing payment instrument.  A string in the format: &#x60;payment_instrument_[0-9a-z]&#x60; | 

### Return type

[**PaymentInstrument**](PaymentInstrument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

