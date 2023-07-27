# Conversion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**Currency**](Currency.md) |  | [optional] 
**to** | [**BankAccountCurrency**](BankAccountCurrency.md) |  | [optional] 
**status** | [**ConversionStatus**](ConversionStatus.md) |  | [optional] 
**expected_amount** | **int** | The expected amount of the conversion in the target currency. The amount is always in the lowest denomination of the target currency, so please be aware of the target currencies _minor unit_. | [optional] 
**rate** | **float** | The conversion rate in the form &#x60;from&#x60; -&gt; &#x60;to&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

