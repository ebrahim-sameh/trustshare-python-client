# BankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the bank_account.  A string in the format &#x60;bank_account_[0-9a-z]&#x60;. | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**currency** | [**BankAccountCurrency**](BankAccountCurrency.md) |  | [optional] 
**account_number** | **str** | The account number of the bank account. | [optional] 
**routing_code** | **str** | The routing code of the bank account. | [optional] 
**routing_code_type** | [**RoutingCodeType**](RoutingCodeType.md) |  | [optional] 
**routing_data** | **object** | An object potentially containing further routing data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

