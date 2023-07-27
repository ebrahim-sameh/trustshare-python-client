# swagger_client.ProjectsApi

All URIs are relative to *https://rest.trustshare.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /v1/projects | Create a Project
[**credit_project**](ProjectsApi.md#credit_project) | **POST** /_sandbox/v1/project/{id}/credit | Credit a Project
[**get_project**](ProjectsApi.md#get_project) | **GET** /v1/project/{id} | Get a Project

# **create_project**
> Project create_project(body, authorization)

Create a Project

Creating a Project allows you to take control of a project account. This account can be used to collect funds from any number of Participants, as well as release funds to any number of Participants.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.V1ProjectsBody() # V1ProjectsBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.

try:
    # Create a Project
    api_response = api_instance.create_project(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ProjectsBody**](V1ProjectsBody.md)|  | 
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.ProjectsApi()
body = swagger_client.IdCreditBody() # IdCreditBody | 
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing project.  A string in the format: `project_[0-9a-z]`

try:
    # Credit a Project
    api_response = api_instance.credit_project(body, authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->credit_project: %s\n" % e)
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

# **get_project**
> Project get_project(authorization, id)

Get a Project

Retrieve an existing project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing project.  A string in the format: `project_[0-9a-z]`

try:
    # Get a Project
    api_response = api_instance.get_project(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your API Key in the format &#x60;[sandbox|live]_api_[0-9a-z]&#x60;. | 
 **id** | **str**| A unique ID of an existing project.  A string in the format: &#x60;project_[0-9a-z]&#x60; | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

