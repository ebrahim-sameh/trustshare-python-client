# SettlementTargetInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID of a participant to use for this intent.  A string in the format: &#x60;participant_[0-9a-z]&#x60;. | [optional] 
**email** | **str** | The email address of the participant in this intent. | [optional] 
**type** | [**ParticipantType**](ParticipantType.md) |  | [optional] 
**name** | **str** | The participant&#x27;s name. | [optional] 
**address** | [**AddressInput**](AddressInput.md) |  | [optional] 
**bank_account** | [**IntentBankAccountInput**](IntentBankAccountInput.md) |  | [optional] 
**business** | [**BusinessInput**](BusinessInput.md) |  | [optional] 
**individual** | [**IndividualInput**](IndividualInput.md) |  | [optional] 
**organisation** | [**OrganisationInput**](OrganisationInput.md) |  | [optional] 
**project_id** | **str** | A unique ID of a project to use as the target for this settlement.  A string in the format: &#x60;project_[0-9a-z]&#x60;. | [optional] 
**metadata** | **object** | A free-form metadata object that you can use to store against the participant. This is incredibly useful for storing a correlation ID that relates to an entity on your own system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

