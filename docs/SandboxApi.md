# swagger_client.SandboxApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_project**](SandboxApi.md#credit_project) | **POST** /_sandbox/v1/project/{id}/credit | Credit a Project

# **credit_project**
> CreditResult credit_project(body, authorization, id)

Credit a Project

__For use in sandbox only.__  Credit a project with an amount of funds. An optional reference can be provided to target a specific checkout.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SandboxApi()
body = swagger_client.IdCreditBody() # IdCreditBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing project.  A string in the format: `project_[0-9a-z]`

try:
    # Credit a Project
    api_response = api_instance.credit_project(body, authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->credit_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdCreditBody**](IdCreditBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing project.  A string in the format: &#x60;project_[0-9a-z]&#x60; | 

### Return type

[**CreditResult**](CreditResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

