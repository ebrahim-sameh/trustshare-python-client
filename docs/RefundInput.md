# RefundInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_id** | **str** | A unique ID of a settlement to refund.  A string in the format: &#x60;settlement_[0-9a-z]&#x60;. | 
**amount** | **int** | The amount to refund in the currencies lowest denomination. | [optional] 
**release_at** | **str** | A date that describes when the funds should be automatically released.  Verification will be eagerly attempted if required. | [optional] 
**reference** | **str** | A reference that should be used for the outbound.  The reference can be up to 18 characters in length and supports &#x60;a-z&#x60;, &#x60;A-Z&#x60;, &#x60;0-9&#x60;, &#x60;-&#x60;, and space characters. This will fall back to your company name if no reference is provided. | [optional] 
**metadata** | **object** | A free-form metadata object that you can use to store against the outbound. This is incredibly useful for storing a correlation ID that relates to an entity on your own system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

