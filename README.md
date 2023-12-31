# swagger-client
Welcome to the trustshare API Reference documentation. Here you can find detailed information about the endpoints we provide as well as the shape of entities within the system.  # Environments The trustshare API has two environments, __Sandbox__ and __Live__. Both environments are available under the same endpoint however API Keys and client secrets are prefixed with the environment name. - A __Sandbox__ API Key will be in the format: `sandbox_api_[0-9a-z]`. - A __Live__ API Key will be in the format: `live_api_[0-9a-z]`.  ## Sandbox Our __Sandbox__ environment endeavours to be as close to the __Live__ environment as possible, however, there are a couple of limitations and features which should be noted. - Card payments take around 7 days to settle into accounts. In __Live__ this is generally closer to 2 days. - Manual inbound payments can only be \"faked\" in __Sandbox__ when they are less-than or equal-to `250,000.00`. - Open Banking in __Sandbox__ will always use a \"Mock Bank\" UI to accept the payment.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.23
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | Your API Key in the format `[sandbox|live]_api_[0-9a-z]`.
id = 'id_example' # str | A unique ID of an existing checkout.  A string in the format: `checkout_[0-9a-z]`

try:
    # Get a Checkout
    api_response = api_instance.get_checkout(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutsApi->get_checkout: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://rest.trustshare.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CheckoutsApi* | [**get_checkout**](docs/CheckoutsApi.md#get_checkout) | **GET** /v1/checkout/{id} | Get a Checkout
*InboundsApi* | [**get_inbound**](docs/InboundsApi.md#get_inbound) | **GET** /v1/inbound/{id} | Get an Inbound
*InvoicesApi* | [**get_invoice**](docs/InvoicesApi.md#get_invoice) | **GET** /v1/invoice/{id} | Get an Invoice
*OutboundsApi* | [**cancel_outbound**](docs/OutboundsApi.md#cancel_outbound) | **POST** /v1/outbound/{id}/cancel | Cancel an Outbound
*OutboundsApi* | [**create_refunds**](docs/OutboundsApi.md#create_refunds) | **POST** /v1/outbounds/refunds | Create Refunds
*OutboundsApi* | [**create_releases**](docs/OutboundsApi.md#create_releases) | **POST** /v1/outbounds/releases | Create Releases
*OutboundsApi* | [**get_outbound**](docs/OutboundsApi.md#get_outbound) | **GET** /v1/outbound/{id} | Get an Outbound
*ParticipantsApi* | [**create_participant**](docs/ParticipantsApi.md#create_participant) | **POST** /v1/participants | Create a Participant
*ParticipantsApi* | [**get_participant**](docs/ParticipantsApi.md#get_participant) | **GET** /v1/participant/{id} | Get a Participant
*ParticipantsApi* | [**get_payout_support**](docs/ParticipantsApi.md#get_payout_support) | **GET** /v1/support/payout | Get Payout Support
*PaymentInstrumentsApi* | [**create_payment_instrument**](docs/PaymentInstrumentsApi.md#create_payment_instrument) | **POST** /v1/payment-instruments | Create a Payment Instrument
*PaymentInstrumentsApi* | [**get_payment_instrument**](docs/PaymentInstrumentsApi.md#get_payment_instrument) | **GET** /v1/payment-instrument/{id} | Get a Payment Instrument
*PaymentIntentsApi* | [**cancel_intent**](docs/PaymentIntentsApi.md#cancel_intent) | **POST** /v1/intent/{id}/cancel | Cancel an Intent
*PaymentIntentsApi* | [**confirm_payment_intent**](docs/PaymentIntentsApi.md#confirm_payment_intent) | **POST** /v1/intent/{id}/confirm | Confirm a Payment Intent
*PaymentIntentsApi* | [**create_payment_intent**](docs/PaymentIntentsApi.md#create_payment_intent) | **POST** /v1/intents/payment | Create a Payment Intent
*PaymentIntentsApi* | [**get_intent**](docs/PaymentIntentsApi.md#get_intent) | **GET** /v1/intent/{id} | Get an Intent
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /v1/projects | Create a Project
*ProjectsApi* | [**credit_project**](docs/ProjectsApi.md#credit_project) | **POST** /_sandbox/v1/project/{id}/credit | Credit a Project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /v1/project/{id} | Get a Project
*SandboxApi* | [**credit_project**](docs/SandboxApi.md#credit_project) | **POST** /_sandbox/v1/project/{id}/credit | Credit a Project
*SettlementsApi* | [**cancel_settlement**](docs/SettlementsApi.md#cancel_settlement) | **POST** /v1/settlement/{id}/cancel | Cancel a Settlement
*SettlementsApi* | [**get_settlement**](docs/SettlementsApi.md#get_settlement) | **GET** /v1/settlement/{id} | Get a Settlement
*SetupIntentsApi* | [**create_setup_intent**](docs/SetupIntentsApi.md#create_setup_intent) | **POST** /v1/intents/setup | Create a Setup Intent
*SetupIntentsApi* | [**get_intent**](docs/SetupIntentsApi.md#get_intent) | **GET** /v1/intent/{id} | Get an Intent
*TransfersApi* | [**create_transfers**](docs/TransfersApi.md#create_transfers) | **POST** /v1/transfers | Create Transfers
*TransfersApi* | [**get_transfer**](docs/TransfersApi.md#get_transfer) | **GET** /v1/transfer/{id} | Get a Transfer
*VerificationsApi* | [**create_verification**](docs/VerificationsApi.md#create_verification) | **POST** /v1/verifications | Create a Verification
*VerificationsApi* | [**get_verification**](docs/VerificationsApi.md#get_verification) | **GET** /v1/verification/{id} | Get a Verification

## Documentation For Models

 - [Address](docs/Address.md)
 - [AddressInput](docs/AddressInput.md)
 - [AddressType](docs/AddressType.md)
 - [BankAccount](docs/BankAccount.md)
 - [BankAccountCurrency](docs/BankAccountCurrency.md)
 - [BankAccountInput](docs/BankAccountInput.md)
 - [Business](docs/Business.md)
 - [BusinessInput](docs/BusinessInput.md)
 - [BusinessType](docs/BusinessType.md)
 - [Checkout](docs/Checkout.md)
 - [CheckoutStatus](docs/CheckoutStatus.md)
 - [CheckoutType](docs/CheckoutType.md)
 - [Collect](docs/Collect.md)
 - [CollectionAccount](docs/CollectionAccount.md)
 - [Confirmation](docs/Confirmation.md)
 - [Conversion](docs/Conversion.md)
 - [ConversionStatus](docs/ConversionStatus.md)
 - [Country](docs/Country.md)
 - [CreditPaymentInput](docs/CreditPaymentInput.md)
 - [CreditResult](docs/CreditResult.md)
 - [CreditTerms](docs/CreditTerms.md)
 - [Currency](docs/Currency.md)
 - [Debit](docs/Debit.md)
 - [DebitStatus](docs/DebitStatus.md)
 - [DepositIntent](docs/DepositIntent.md)
 - [Fee](docs/Fee.md)
 - [IdConfirmBody](docs/IdConfirmBody.md)
 - [IdCreditBody](docs/IdCreditBody.md)
 - [Inbound](docs/Inbound.md)
 - [InboundStatus](docs/InboundStatus.md)
 - [InboundType](docs/InboundType.md)
 - [Individual](docs/Individual.md)
 - [IndividualInput](docs/IndividualInput.md)
 - [Intent](docs/Intent.md)
 - [IntentBankAccountInput](docs/IntentBankAccountInput.md)
 - [IntentOutputType](docs/IntentOutputType.md)
 - [IntentStatus](docs/IntentStatus.md)
 - [IntentType](docs/IntentType.md)
 - [IntentsPaymentBody](docs/IntentsPaymentBody.md)
 - [IntentsSetupBody](docs/IntentsSetupBody.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceStatus](docs/InvoiceStatus.md)
 - [KnownParticipant](docs/KnownParticipant.md)
 - [Limit](docs/Limit.md)
 - [LinkIntent](docs/LinkIntent.md)
 - [Organisation](docs/Organisation.md)
 - [OrganisationInput](docs/OrganisationInput.md)
 - [OrganisationType](docs/OrganisationType.md)
 - [Outbound](docs/Outbound.md)
 - [OutboundFailureReason](docs/OutboundFailureReason.md)
 - [OutboundPausedReason](docs/OutboundPausedReason.md)
 - [OutboundResult](docs/OutboundResult.md)
 - [OutboundStatus](docs/OutboundStatus.md)
 - [OutboundType](docs/OutboundType.md)
 - [OutboundsRefundsBody](docs/OutboundsRefundsBody.md)
 - [OutboundsReleasesBody](docs/OutboundsReleasesBody.md)
 - [ParticipantInput](docs/ParticipantInput.md)
 - [ParticipantStatus](docs/ParticipantStatus.md)
 - [ParticipantType](docs/ParticipantType.md)
 - [PaymentInstrument](docs/PaymentInstrument.md)
 - [PaymentInstrumentStatus](docs/PaymentInstrumentStatus.md)
 - [PaymentInstrumentType](docs/PaymentInstrumentType.md)
 - [PaymentIntent](docs/PaymentIntent.md)
 - [PaymentType](docs/PaymentType.md)
 - [Person](docs/Person.md)
 - [PersonInput](docs/PersonInput.md)
 - [PersonType](docs/PersonType.md)
 - [Project](docs/Project.md)
 - [ProjectAccount](docs/ProjectAccount.md)
 - [ProjectRoutingCodeType](docs/ProjectRoutingCodeType.md)
 - [ProjectRoutingData](docs/ProjectRoutingData.md)
 - [ProjectStatus](docs/ProjectStatus.md)
 - [ProjectTransferIn](docs/ProjectTransferIn.md)
 - [ProjectTransferOut](docs/ProjectTransferOut.md)
 - [ProjectTransfers](docs/ProjectTransfers.md)
 - [ProjectType](docs/ProjectType.md)
 - [RefundInput](docs/RefundInput.md)
 - [ReleaseInput](docs/ReleaseInput.md)
 - [Requirement](docs/Requirement.md)
 - [Requirements](docs/Requirements.md)
 - [RoutingCodeType](docs/RoutingCodeType.md)
 - [SessionIntent](docs/SessionIntent.md)
 - [Settlement](docs/Settlement.md)
 - [SettlementInput](docs/SettlementInput.md)
 - [SettlementIntent](docs/SettlementIntent.md)
 - [SettlementStatus](docs/SettlementStatus.md)
 - [SettlementTargetInput](docs/SettlementTargetInput.md)
 - [SettlementType](docs/SettlementType.md)
 - [SetupIntent](docs/SetupIntent.md)
 - [SetupIntentType](docs/SetupIntentType.md)
 - [TradeAccount](docs/TradeAccount.md)
 - [Transfer](docs/Transfer.md)
 - [TransferInput](docs/TransferInput.md)
 - [TransferResult](docs/TransferResult.md)
 - [TransferSourceOrTarget](docs/TransferSourceOrTarget.md)
 - [TransferSourceOrTargetInput](docs/TransferSourceOrTargetInput.md)
 - [TransferStatus](docs/TransferStatus.md)
 - [TransferSubType](docs/TransferSubType.md)
 - [TransferType](docs/TransferType.md)
 - [V1ParticipantsBody](docs/V1ParticipantsBody.md)
 - [V1PaymentinstrumentsBody](docs/V1PaymentinstrumentsBody.md)
 - [V1ProjectsBody](docs/V1ProjectsBody.md)
 - [V1TransfersBody](docs/V1TransfersBody.md)
 - [V1VerificationsBody](docs/V1VerificationsBody.md)
 - [Verification](docs/Verification.md)
 - [VerificationStatus](docs/VerificationStatus.md)
 - [VerificationType](docs/VerificationType.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

support@trustshare.co
