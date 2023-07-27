# Inbound

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the inbound.  A string in the format &#x60;inbound_[0-9a-z]&#x60;. | [optional] 
**created_at** | **str** | The date the project was created. | [optional] 
**updated_at** | **str** | The date the project was last updated. | [optional] 
**project_id** | **str** | The unique ID of the project which this inbound funds. | [optional] 
**checkout_id** | **str** | The unique ID of the checkout that this inbound has been reconciled against.  If we were unable to reconcile the inbound to a specific checkout this value will be null. | [optional] 
**transfer** | [**ProjectTransferIn**](ProjectTransferIn.md) |  | [optional] 
**type** | [**InboundType**](InboundType.md) |  | [optional] 
**status** | [**InboundStatus**](InboundStatus.md) |  | [optional] 
**amount** | **int** | The amount of the inbound. | [optional] 
**reference** | **str** | The reference that was used for the inbound.  This will be &#x60;null&#x60; if no reference is provided by the buyer or the inbound is not a bank transfer, ie. manual or Open Banking initiated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

