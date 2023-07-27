# IntentsPaymentBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IntentType**](IntentType.md) |  | 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**_from** | [**ParticipantInput**](ParticipantInput.md) |  | [optional] 
**project_id** | **str** | Optionally provide a &#x60;project_id&#x60; to target the payemnt at an existing project account. If no &#x60;project_id&#x60; is provided, a new Project will be automatically provisioned for you. | [optional] 
**fee_flat** | **int** | A flat fee to charge the buyer Participant on successfully completing a Checkout. | [optional] 
**fee_percentage** | **float** | A fee percentage to charge the buyer Participant on successfully completing a Checkout. Fee percentages must be provided as a fraction, ie. 1.5% as 0.015. | [optional] 
**settlements** | [**list[SettlementInput]**](SettlementInput.md) | A list of settlements that the buyer Participant must fulfill. | 
**redirect_url** | **str** | For both &#x60;checkout&#x60; and &#x60;payment_link&#x60; intent types you can provide a redirect URL that the user will be directed to at the end of the checkout process.  The URL will have the &#x60;project_id&#x60; and &#x60;checkout_id&#x60; appended to the query string. For example, given the redirect URL &#x60;https://example.com/complete&#x60;, your users will be redirected to &#x60;https://example.com/complete?checkout_id&#x3D;{checkout_id}&amp;project_id&#x3D;{project_id}&#x60;.  &lt;Note&gt;   When using the SDK to confirm a &#x60;checkout&#x60; type payment intent, the   parent page — ie. the page opening the modal — will be redirected to this URL. &lt;/Note&gt; | [optional] 
**metadata** | **object** | A free-form metadata object that you can use to store against the intent. This is incredibly useful for storing a correlation ID that relates to an entity on your own system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

