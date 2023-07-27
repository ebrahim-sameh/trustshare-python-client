# Checkout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the checkout.  A string in the format &#x60;checkout_[0-9a-z]&#x60;. | [optional] 
**created_at** | **str** | The date the checkout was created. | [optional] 
**updated_at** | **str** | The date the checkout was last updated. | [optional] 
**type** | [**CheckoutType**](CheckoutType.md) |  | [optional] 
**status** | [**CheckoutStatus**](CheckoutStatus.md) |  | [optional] 
**participant** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**outstanding** | **int** | The outstanding amount on the checkout to compare against the original amount set by the payment intent.  Signifies if the checkout has been under or overfunded. In the case of overfunding, the value will be negative. | [optional] 
**amount** | **int** | The amount of the checkout. | [optional] 
**reference** | **str** | The unique reference for the checkout. | [optional] 
**intent_id** | **str** | The unique ID of the intent which caused the checkout to be created. This value will be null if the checkout was created via our Direct mechanism. | [optional] 
**project_id** | **str** | The unique ID of the project which this checkout will fund. | [optional] 
**transfers** | [**list[Transfer]**](Transfer.md) | The &#x60;transfers&#x60; key historically used to represent the fees associated with the given checkout, since these fees are \&quot;transfered\&quot; to the partner revenue accounts.  These fee transfers will now be listed under the &#x60;fees&#x60; key.  While &#x60;transfers&#x60; going forward, will globally denote within-system fund movements initiated by the API user. | [optional] 
**fees** | [**list[Fee]**](Fee.md) | A list of fee transfers associated with the checkout. | [optional] 
**settlements** | [**list[Settlement]**](Settlement.md) | A list of settlements that were targeted by the checkout. | [optional] 
**debits** | [**list[Debit]**](Debit.md) | A list of direct debit payments that have been scheduled by the checkout. | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the payment intent that caused this checkout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

