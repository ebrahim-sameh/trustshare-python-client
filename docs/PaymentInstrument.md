# PaymentInstrument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the payment instrument.  A string in the format: &#x60;payment_instrument_[0-9a-z]&#x60;. | [optional] 
**created_at** | **str** | The date the payment instrument was created. | [optional] 
**updated_at** | **str** | The date the payment instrument was last updated. | [optional] 
**status** | [**PaymentInstrumentStatus**](PaymentInstrumentStatus.md) |  | [optional] 
**type** | [**PaymentInstrumentType**](PaymentInstrumentType.md) |  | [optional] 
**owner** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**trade_account** | [**TradeAccount**](TradeAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

