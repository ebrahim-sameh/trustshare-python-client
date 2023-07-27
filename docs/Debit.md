# Debit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the debit.  A string in the format &#x60;debit_[0-9a-z]&#x60;. | [optional] 
**status** | [**DebitStatus**](DebitStatus.md) |  | [optional] 
**scheduled_at** | **str** | The date trustshare will attempt to take payment from the payer&#x27;s bank account. | [optional] 
**amount** | **int** | The amount of the debit payment. | [optional] 
**checkout_id** | **str** | A unique ID for the checkout this debit has been created for. | [optional] 
**project_id** | **str** | The unique ID of the project which this debit will fund. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

