# Project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the project.  A string in the format &#x60;project_[0-9a-z]&#x60;. | [optional] 
**created_at** | **str** | The date the project was created. | [optional] 
**updated_at** | **str** | The date the project was last updated. | [optional] 
**type** | [**ProjectType**](ProjectType.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | [optional] 
**balance** | **int** | The sum of all unreconciled inbounds and funding settlement balances currently in the underlying account. | [optional] 
**checkouts** | [**list[Checkout]**](Checkout.md) | A list of [checkouts](/resources/checkouts) that have funded the project. | [optional] 
**settlements** | [**list[Settlement]**](Settlement.md) | A list of [settlements](/resources/settlements) against the project. | [optional] 
**inbounds** | [**list[Inbound]**](Inbound.md) | A list of [inbounds](/resources/inbounds) which denote physical receipt of funds into the project account. | [optional] 
**outbounds** | [**list[Outbound]**](Outbound.md) | A list of [outbounds](/resources/outbounds) that have sent funds from the project account. | [optional] 
**transfers** | [**ProjectTransfers**](ProjectTransfers.md) |  | [optional] 
**collect** | [**Collect**](Collect.md) |  | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the project. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

