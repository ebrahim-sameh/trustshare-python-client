# SettlementIntent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The date the settlement intent was created. | [optional] 
**updated_at** | **str** | The date the settlement intent was last updated. | [optional] 
**to** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**type** | [**SettlementType**](SettlementType.md) |  | [optional] 
**amount** | **int** | The amount of the settlement intent. | [optional] 
**description** | **str** | A description of the reason for the settlement. | [optional] 
**summary** | **str** | An optional summary of the settlement. | [optional] 
**fee_flat** | **int** | The flat fee the beneficiary Participant will be pay on each release from the settlement. | [optional] 
**fee_percentage** | **float** | The percentage fee the beneficiary Participant will pay on each release from the settlement. | [optional] 
**tax_flat** | **int** | The pre-computed flat tax charge that has been added to the value of the settlement. The settlement amount is inclusive of this value. | [optional] 
**tax_percentage** | **float** | The tax charge that has been added to the value of the settlement, expressed as a percentage. The settlement amount is inclusive of the computed percentage amount. | [optional] 
**required_by** | **str** | A date that describes when the funds are required. If the funds are required at a future date, the amount will not be included in the total on the Checkout UI.  You can collect funds against this settlement at a later date by creating a new payment intent that targets the settlement ID when the buyer Participant agrees to the Checkout. | [optional] 
**release_at** | **str** | The date that describes when the funds will be automatically released.  Verification will be eagerly attempted if required. | [optional] 
**reference** | **str** | The reference that will be used for releases from this settlement. | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the settlement intent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

