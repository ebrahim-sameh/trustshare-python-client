# swagger_client.ParticipantsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_participant**](ParticipantsApi.md#create_participant) | **POST** /v1/participants | Create a Participant
[**get_participant**](ParticipantsApi.md#get_participant) | **GET** /v1/participant/{id} | Get a Participant
[**get_payout_support**](ParticipantsApi.md#get_payout_support) | **GET** /v1/support/payout | Get Payout Support

# **create_participant**
> KnownParticipant create_participant(body, authorization)

Create a Participant

Optionally, you can pre-create a participant to use in an intent. The returned unique ID should be used in the intent creation call. The minimum requirement for creating a participant is an email address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParticipantsApi()
body = swagger_client.V1ParticipantsBody() # V1ParticipantsBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create a Participant
    api_response = api_instance.create_participant(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParticipantsApi->create_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ParticipantsBody**](V1ParticipantsBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**KnownParticipant**](KnownParticipant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participant**
> KnownParticipant get_participant(authorization, id)

Get a Participant

Retrieve an existing participant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParticipantsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing participant.  A string in the format: `participant_[0-9a-z]`

try:
    # Get a Participant
    api_response = api_instance.get_participant(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParticipantsApi->get_participant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing participant.  A string in the format: &#x60;participant_[0-9a-z]&#x60; | 

### Return type

[**KnownParticipant**](KnownParticipant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_support**
> Requirements get_payout_support(country, currency)

Get Payout Support

Given a country/currency pairing, returns whether the pair is supported along with the required fields that must be provided to the API when including a bank account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ParticipantsApi()
country = swagger_client.Country() # Country | The country the bank account is held in.
currency = swagger_client.BankAccountCurrency() # BankAccountCurrency | The currency the bank account is held in.

try:
    # Get Payout Support
    api_response = api_instance.get_payout_support(country, currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParticipantsApi->get_payout_support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | [**Country**](.md)| The country the bank account is held in. | 
 **currency** | [**BankAccountCurrency**](.md)| The currency the bank account is held in. | 

### Return type

[**Requirements**](Requirements.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

