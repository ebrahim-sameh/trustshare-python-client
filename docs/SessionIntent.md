# SessionIntent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the created intent. | [optional] 
**created_at** | **str** | The date the setup intent was created. | [optional] 
**updated_at** | **str** | The date the setup intent was last updated. | [optional] 
**participant** | [**KnownParticipant**](KnownParticipant.md) |  | [optional] 
**client_secret** | **str** | The client secret for the intent.  &lt;Note&gt;   This secret should __never__ be stored on a backend system and should always   be directly passed down to the expected participant&#x27;s device. &lt;/Note&gt; | [optional] 
**status** | [**IntentStatus**](IntentStatus.md) |  | [optional] 
**type** | [**IntentOutputType**](IntentOutputType.md) |  | [optional] 
**metadata** | **object** | The metadata that was provided at the creation of the setup intent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

