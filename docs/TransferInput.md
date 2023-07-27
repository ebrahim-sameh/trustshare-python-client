# TransferInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount to transfer in the currency&#x27;s lowest denomination. | 
**fee_flat** | **int** | A flat fee to charge on successfully completing a Transfer. | [optional] 
**fee_percentage** | **float** | A fee percentage to charge on successfully completing a Transfer. Fee percentages must be provided as a fraction, ie. 1.5% as 0.015. | [optional] 
**_from** | [**TransferSourceOrTargetInput**](TransferSourceOrTargetInput.md) |  | 
**to** | [**TransferSourceOrTargetInput**](TransferSourceOrTargetInput.md) |  | 
**release_at** | **str** | A date that describes when the funds should be automatically transfered. | [optional] 
**metadata** | **object** | A free-form metadata object that you can use to store against the transfer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

