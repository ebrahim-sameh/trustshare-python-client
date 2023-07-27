# Transfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the transfer.  A string in the format: &#x60;transfer_[0-9a-z]&#x60;. | [optional] 
**created_at** | **str** | The date the transfer was created. | [optional] 
**updated_at** | **str** | The date the transfer was last updated. | [optional] 
**type** | [**TransferType**](TransferType.md) |  | [optional] 
**subtype** | [**TransferSubType**](TransferSubType.md) |  | [optional] 
**status** | [**TransferStatus**](TransferStatus.md) |  | [optional] 
**amount** | **int** | The amount of the transfer. | [optional] 
**_from** | [**TransferSourceOrTarget**](TransferSourceOrTarget.md) |  | [optional] 
**to** | [**TransferSourceOrTarget**](TransferSourceOrTarget.md) |  | [optional] 
**inbound_id** | **str** | The unique ID of the inbound that describes funds entering the target project as a result of this transfer. | [optional] 
**outbound_id** | **str** | The unique ID of the outbound that describes funds leaving the source project as a result of this transfer. | [optional] 
**release_at** | **str** | The date that describes when the funds will be automatically transfered. | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the transfer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

