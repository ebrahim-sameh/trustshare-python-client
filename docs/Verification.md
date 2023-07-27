# Verification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID of the verification.  A string in the format: &#x60;verification_[0-9a-z]&#x60;. | [optional] 
**type** | [**VerificationType**](VerificationType.md) |  | [optional] 
**status** | [**VerificationStatus**](VerificationStatus.md) |  | [optional] 
**participant** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**client_secret** | **str** | The client secret for the verification.  &lt;Note&gt;   This secret should __never__ be stored on a backend system and should   always be directly passed down to the expected participant&#x27;s device. &lt;/Note&gt; | [optional] 
**redirect_url** | **str** | The redirect URL supplied at the creation of the verification. | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the verification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

