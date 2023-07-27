# V1VerificationsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID of an existing participant that needs to be verified.  A string in the format: &#x60;participant_[0-9a-z]&#x60; | [optional] 
**type** | [**ParticipantType**](ParticipantType.md) |  | [optional] 
**email** | **str** | The email of the participant to verify. | [optional] 
**name** | **str** | The name of the participant to verify. | [optional] 
**address** | [**AddressInput**](AddressInput.md) |  | [optional] 
**bank_account** | [**BankAccountInput**](BankAccountInput.md) |  | [optional] 
**business** | [**BusinessInput**](BusinessInput.md) |  | [optional] 
**individual** | [**IndividualInput**](IndividualInput.md) |  | [optional] 
**organisation** | [**OrganisationInput**](OrganisationInput.md) |  | [optional] 
**redirect_url** | **str** | You can provide a redirect URL that the user will be directed to at the end of the verification process.  The URL will have the &#x60;verification_id&#x60; appended to the query string. For example, given the redirect URL &#x60;https://example.com/complete&#x60;, your users will be redirected to &#x60;https://example.com/complete?verification_id&#x3D;{verification_id}&#x60;.  &lt;Note&gt;   When using the SDK to confirm a &#x60;verification&#x60;, the   parent page — ie. the page opening the modal — will be redirected to this URL. &lt;/Note&gt; | [optional] 
**metadata** | **object** | A free-form metadata object that you can use to store against the intent. This is incredibly useful for storing a correlation ID that relates to an entity on your own system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

