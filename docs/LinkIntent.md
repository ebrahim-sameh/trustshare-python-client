# LinkIntent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the created intent. | [optional] 
**created_at** | **str** | The date the payment intent was created. | [optional] 
**updated_at** | **str** | The date the payment intent was last updated. | [optional] 
**project_id** | **str** | The unique ID of the project which this intent targets. | [optional] 
**_from** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**url** | **str** | The URL that can be shared to complete this payment. | [optional] 
**status** | [**IntentStatus**](IntentStatus.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**type** | [**IntentOutputType**](IntentOutputType.md) |  | [optional] 
**fee_flat** | **int** | A flat fee to charge the buyer Participant on successfully completing the intent.  Fees are calculated in the following way: (&#x60;total&#x60; * (1 + &#x60;fee_percentage&#x60;)) + &#x60;fee_flat&#x60;. | [optional] 
**fee_percentage** | **float** | A fee percentage to charge the buyer Participant on successfully completing the intent. Fee percentages must be provided as a fraction, ie. 1.5% as 0.015.  Fees are calculated in the following way: (&#x60;total&#x60; * (1 + &#x60;fee_percentage&#x60;)) + &#x60;fee_flat&#x60;. | [optional] 
**settlements** | [**list[SettlementIntent]**](SettlementIntent.md) | A list of settlement intents. These describe the line items that will be displayed on the Checkout UI. | [optional] 
**redirect_url** | **str** | The redirect URL supplied at the creation of the intent. | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the payment intent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

