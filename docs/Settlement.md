# Settlement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the settlement.  A string in the format &#x60;settlement_[0-9a-z]&#x60;. | [optional] 
**created_at** | **str** | The date the settlement was created. | [optional] 
**updated_at** | **str** | The date the settlement was last updated. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**status** | [**SettlementStatus**](SettlementStatus.md) |  | [optional] 
**type** | [**SettlementType**](SettlementType.md) |  | [optional] 
**project_id** | **str** | The unique ID of the project which this settlement belongs to. | [optional] 
**_from** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**to** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**amount** | **int** | The amount of the settlement. | [optional] 
**description** | **str** | The provided description of the settlement. | [optional] 
**summary** | **str** | The provided summary of the settlement. | [optional] 
**balance** | **int** | The current balance of the settlement. The balance for a settlement is calculated in the following way:  &#x60;balance&#x60; &#x3D; &#x60;received&#x60; - (&#x60;released&#x60; + &#x60;refunded&#x60;)  A negative balance infers that funds have been released however we are still waiting for funds to reconcile into the settlement. | [optional] 
**fee_flat** | **int** | The flat fee to charge the beneficiary Participant on successfully releasing funds from the settlement. | [optional] 
**fee_percentage** | **float** | The fee percentage to charge the beneficiary Participant on successfully releasing funds from the settlement. | [optional] 
**tax_flat** | **int** | The pre-computed flat tax charge that has been added to the value of the settlement. The settlement amount is inclusive of this value. | [optional] 
**tax_percentage** | **float** | The tax charge that has been added to the value of the settlement, expressed as a percentage. The settlement amount is inclusive of the computed percentage amount. | [optional] 
**required_by** | **str** | The date that describes when the funds are required. | [optional] 
**release_at** | **str** | The date that describes when the funds will be automatically released.  Verification will be eagerly attempted if required. | [optional] 
**reference** | **str** | The reference that will be used for releases from this settlement. | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the underlying settlement intent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

