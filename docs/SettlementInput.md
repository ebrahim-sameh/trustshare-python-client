# SettlementInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An ID of an existing settlement to target, allowing a user to Checkout against a settlement with a discrepancy or a settlement required at a future date.  A string in the format &#x60;settlement_[0-9a-z]&#x60;. | [optional] 
**type** | [**SettlementType**](SettlementType.md) |  | [optional] 
**to** | [**SettlementTargetInput**](SettlementTargetInput.md) |  | [optional] 
**amount** | **int** | The amount of the settlement described in the lowest denomination for the intent&#x27;s currency. ie, £1,000.00 should be provided as &#x60;100000&#x60;. | [optional] 
**description** | **str** | A description of the settlement that will be displayed as a line item in the Checkout UI. | [optional] 
**summary** | **str** | A further summary of the settlement that will be displayed under the line item in the Checkout UI. | [optional] 
**fee_flat** | **int** | A flat fee to charge the beneficiary Participant on successfully releasing funds from the settlement.  Fees are calculated in the following way: (&#x60;total&#x60; * (1 + &#x60;fee_percentage&#x60;)) + &#x60;fee_flat&#x60;. | [optional] 
**fee_percentage** | **float** | A fee percentage to charge the beneficiary Participant on successfully releasing funds from the settlement. Fee percentages must be provided as a fraction, ie. 1.5% as 0.015.  Fees are calculated in the following way: (&#x60;total&#x60; * (1 + &#x60;fee_percentage&#x60;)) + &#x60;fee_flat&#x60;. | [optional] 
**tax_flat** | **int** | A pre-computed flat tax charge that has been added to the value of the settlement. The settlement amount should be inclusive of this value.  Flat tax amount must be described in the lowest denomination for the intent&#x27;s currency. ie, £20.00 should be provided as &#x60;2000&#x60;.  Assuming a 20% tax rate and a line item for a value of £100, &#x60;amount&#x60; and &#x60;tax_flat&#x60; should be: &#x60;&#x60;&#x60;   {     ...     \&quot;amount\&quot;: 12000,     \&quot;tax_flat\&quot;: 2000,     ...   } &#x60;&#x60;&#x60;  &#x60;tax_flat&#x60; and &#x60;tax_percentage&#x60; are mutually exlusive for the same settlement. | [optional] 
**tax_percentage** | **float** | A pre-computed tax charge that has been added to the value of the settlement, expressed as a percentage. The settlement amount should be inclusive of the computed percentage amount.  Tax percentages must be provided as a fraction, ie. 20% as 0.2.  Assuming a 20% tax rate and a line item for a value of £100, &#x60;amount&#x60; and &#x60;tax_percentage&#x60; should be: &#x60;&#x60;&#x60;   {     ...     \&quot;amount\&quot;: 12000,     \&quot;tax_percentage\&quot;: 0.2,     ...   } &#x60;&#x60;&#x60;  &#x60;tax_flat&#x60; and &#x60;tax_percentage&#x60; are mutually exlusive for the same settlement. | [optional] 
**required_by** | **str** | A date that describes when the funds are required. If the funds are required at a future date, the amount will not be included in the total on the Checkout UI.  You can collect funds against this settlement at a later date by creating a new payment intent that targets the settlement ID when the buyer Participant agrees to the Checkout. | [optional] 
**release_at** | **str** | A date that describes when the funds should be automatically released.  Verification will be eagerly attempted if required. | [optional] 
**reference** | **str** | A reference that will be used for releases from this settlement and will appear on a beneficiary&#x27;s bank statement. | [optional] 
**metadata** | **object** | A free-form metadata object that you can use to store against the settlement. This is incredibly useful for storing a correlation ID that relates to an entity on your own system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

