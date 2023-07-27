# Outbound

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the outbound.  A string in the format &#x60;outbound_[0-9a-z]&#x60;. | [optional] 
**created_at** | **str** | The date the outbound was created. | [optional] 
**updated_at** | **str** | The date the outbound was last updated. | [optional] 
**release_at** | **str** | The date that describes when the funds will be automatically released.  Verification will be eagerly attempted if required. | [optional] 
**project_id** | **str** | The project ID the outbound was created against. | [optional] 
**settlement_id** | **str** | The settlement ID the outbound was created against. In the event funds were released directly from a project, this value will be null. | [optional] 
**type** | [**OutboundType**](OutboundType.md) |  | [optional] 
**status** | [**OutboundStatus**](OutboundStatus.md) |  | [optional] 
**amount** | **int** | The amount of the outbound. | [optional] 
**to** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**transfers** | [**list[Transfer]**](Transfer.md) | The &#x60;transfers&#x60; key historically used to represent the fees associated with the given outbound, since these fees are \&quot;transfered\&quot; to the partner revenue accounts.  These fee transfers will now be listed under the &#x60;fees&#x60; key.  While &#x60;transfers&#x60; going forward, will globally denote within-system fund movements initiated by the API user. | [optional] 
**fees** | [**list[Fee]**](Fee.md) | A list of any fees created as the result of the outbound. | [optional] 
**transfer** | [**ProjectTransferOut**](ProjectTransferOut.md) |  | [optional] 
**conversion** | [**Conversion**](Conversion.md) |  | [optional] 
**paused_reason** | [**OutboundPausedReason**](OutboundPausedReason.md) |  | [optional] 
**failure_reason** | [**OutboundFailureReason**](OutboundFailureReason.md) |  | [optional] 
**reference** | **str** | The reference that will be used for the outbound.  The reference can be up to 18 characters in length and supports &#x60;a-z&#x60;, &#x60;A-Z&#x60;, &#x60;0-9&#x60;, &#x60;-&#x60;, and space characters. | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the release or refund. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

