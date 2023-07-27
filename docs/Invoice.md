# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID for the invoice.  A string in the format &#x60;invoice_[0-9a-z]&#x60;. | [optional] 
**created_at** | **str** | The date the invoice was created. | [optional] 
**updated_at** | **str** | The date the invoice was last updated. | [optional] 
**status** | [**InvoiceStatus**](InvoiceStatus.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**intent_id** | **str** | The unique ID of the intent which caused the invoice to be created. | [optional] 
**project_id** | **str** | The project ID the invoice was created against. | [optional] 
**participant** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**settlements** | [**list[Settlement]**](Settlement.md) | A list of settlements against the invoice. | [optional] 
**collect** | [**Collect**](Collect.md) |  | [optional] 
**reference** | **str** | The unique reference for the invoice. This should be used for all bank transfers targeting this invoice. | [optional] 
**subtotal** | **int** | The invoice value denominated in the smallest unit for the currency. E.g. pence and cents. | [optional] 
**fee** | **int** | The buyer fees specified for the invoice intent, denominated in the smallest unit for the currency. E.g. pence and cents. | [optional] 
**total** | **int** | The full payable amount for the invoice (subtotal + fee), denominated in the smallest unit for the currency. E.g. pence and cents. | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the payment intent that caused this invoice. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

