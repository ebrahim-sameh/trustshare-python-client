# CollectionAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iban** | **str** | The IBAN of the collection account. | [optional] 
**account_number** | **str** | The account number of the collection account. For EUR accounts, this will be &#x60;null&#x60;. | [optional] 
**routing_data** | [**list[ProjectRoutingData]**](ProjectRoutingData.md) | Object array containing account routing information required to make payments to the collection account. The below list describes the types of &#x60;routing_data&#x60; you can receive for each collection currency.  - &#x60;usd&#x60; - the type can be &#x60;ach&#x60;, &#x60;wire&#x60;, or &#x60;bic_swift&#x60; - &#x60;eur&#x60; - the type will be &#x60;bic_swift&#x60; - &#x60;gbp&#x60; - the type can be &#x60;sort_code&#x60;, or &#x60;bic_swift&#x60; | [optional] 
**reference** | **str** | The payment reference __must__ be used if defined, otherwise the payment might not be reconciled correctly. | [optional] 
**metadata** | **object** | Collection account metadata associated with sending payments, such as bank name and address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

