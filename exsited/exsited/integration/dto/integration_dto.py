from dataclasses import dataclass

from exsited.exsited.common.dto.common_dto import PaginationDTO
from exsited.sdlize.ab_base_dto import ABBaseDTO


@dataclass(kw_only=True)
class IntegrationConnectionDisableResponseDTO(ABBaseDTO):
    message: str = None


@dataclass(kw_only=True)
class IntegrationConnectionEnableResponseDTO(ABBaseDTO):
    message: str = None


@dataclass(kw_only=True)
class IntegrationConnectionDTO(ABBaseDTO):
    status: str = None
    uuid: str = None
    integrationPartner: str = None
    remoteInstanceId: str = None
    remoteInstanceName: str = None
    clientId: str = None
    clientSecret: str = None
    accessToken: str = None
    refreshToken: str = None


@dataclass(kw_only=True)
class IntegrationConnectionCreateRequestDTO(ABBaseDTO):
    provider: str = None
    remoteInstanceId: str = None
    remoteInstanceCode: str = None
    remoteInstanceName: str = None
    remoteInstanceDisplay: str = None
    integrationClientId: str = None
    integrationClientSecret: str = None
    integrationAccessToken: str = None
    integrationRefreshToken: str = None
    tokenType: str = None
    expiresIn: str = None
    accountServer: str = None
    apiDomain: str = None
    supportingFields: str = None
    userName: str = None
    userPassword: str = None
    requireAuthentication: bool = None
    state: str = None
    companyFile: str = None
    companyName: str = None


@dataclass(kw_only=True)
class IntegrationAutomationDTO(ABBaseDTO):
    checkOn: str = None
    checkOnMinutes: str = None
    additionalCriteria: str = None
    appliesTo: str = None
    appliesToFunction: str = None
    automationType: str = None
    code: str = None
    customDay: str = None
    customDayTime: str = None
    customTime: str = None
    description: str = None
    direction: str = None
    displayName: str = None
    name: str = None
    performFunction: str = None
    provider: str = None
    status: str = None
    uuid: str = None
    triggerConditionText: str = None
    performActionText: str = None
    checkOnText: str = None


@dataclass(kw_only=True)
class PartnerFunctionDTO(ABBaseDTO):
    uuid: str = None
    name: str = None
    description: str = None
    direction: str = None
    eventName: str = None
    providerName: str = None
    objectName: str = None
    mappingId: str = None
    enabled: str = None
    preRunScriptId: str = None
    postRunScriptId: str = None
    tag: str = None
    created: str = None
    updated: str = None
    objectMapping: str = None


@dataclass(kw_only=True)
class XeroExportSettingsDTO(ABBaseDTO):
    accountToXeroEnabled: str = None
    accountToXeroTaxEnable: str = None
    itemToXeroEnabled: str = None
    productToXeroSalesRevenueEnable: str = None
    productToXeroTaxEnable: str = None
    invoiceToXeroEnabled: str = None
    invoiceToXeroSalesRevenueEnable: str = None
    invoiceToXeroTaxEnable: str = None
    paymentToXeroEnabled: str = None
    creditNoteToXeroEnabled: str = None
    refundToXeroEnabled: str = None
    purchaseOrderToXeroEnabled: str = None
    purchaseOrderToXeroTaxEnable: str = None
    purchaseInvoiceToXeroEnabled: str = None
    purchaseInvoiceToXeroTaxEnable: str = None
    purchasePaymentToXeroEnabled: str = None
    purchasePaymentToXeroTaxEnable: str = None
    purchaseCreditNoteToXeroEnabled: str = None
    purchaseRefundToXeroEnabled: str = None


@dataclass(kw_only=True)
class XeroImportSettingsDTO(ABBaseDTO):
    accountFromXeroEnabled: str = None
    accountToXeroTaxEnable: str = None
    itemFromXeroEnabled: str = None
    productFromXeroTaxEnable: str = None
    invoiceFromXeroEnabled: str = None
    invoiceFromXeroTaxEnable: str = None
    paymentFromXeroEnabled: str = None
    creditNoteFromXeroEnabled: str = None
    refundFromXeroEnabled: str = None
    purchaseOrderFromXeroEnabled: str = None
    purchaseOrderFromXeroTaxEnable: str = None
    purchaseBillFromXeroEnabled: str = None
    purchaseBillFromXeroTaxEnable: str = None
    purchasePaymentFromXeroEnabled: str = None
    purchaseCreditNoteFromXeroEnabled: str = None
    purchaseRefundFromXeroEnabled: str = None


@dataclass(kw_only=True)
class XeroAccountDTO(ABBaseDTO):
    provider: str = None
    accountSyncToXero: str = None
    export: XeroExportSettingsDTO = None
    import_: XeroImportSettingsDTO = None

    _custom_field_mapping = {
        "import": "import_"
    }


@dataclass(kw_only=True)
class XeroItemDTO(ABBaseDTO):
    provider: str = None
    itemSyncToXero: str = None
    export: XeroExportSettingsDTO = None
    import_: XeroImportSettingsDTO = None

    _custom_field_mapping = {
        "import": "import_"
    }


@dataclass(kw_only=True)
class XeroTransactionDTO(ABBaseDTO):
    provider: str = None
    invoiceSyncToXero: str = None
    paymentSyncToXero: str = None
    creditNoteSyncToXero: str = None
    refundSyncToXero: str = None
    export: XeroExportSettingsDTO = None
    import_: XeroImportSettingsDTO = None

    _custom_field_mapping = {
        "import": "import_"
    }


@dataclass(kw_only=True)
class XeroPurchaseDTO(ABBaseDTO):
    provider: str = None
    purchaseOrderSyncToXero: str = None
    purchaseInvoiceSyncToXero: str = None
    purchasePaymentSyncToXero: str = None
    export: XeroExportSettingsDTO = None
    import_: XeroImportSettingsDTO = None

    _custom_field_mapping = {
        "import": "import_"
    }


@dataclass(kw_only=True)
class XeroIntegrationDataDTO(ABBaseDTO):
    account: XeroAccountDTO = None
    item: XeroItemDTO = None
    transaction: XeroTransactionDTO = None
    purchase: XeroPurchaseDTO = None


@dataclass(kw_only=True)
class XeroIntegrationConfigurationResponseDTO(ABBaseDTO):
    integration: XeroIntegrationDataDTO = None


@dataclass(kw_only=True)
class PartnerFunctionListResponseDTO(ABBaseDTO):
    partnerFunctions: list[PartnerFunctionDTO] = None
    pagination: PaginationDTO = None

@dataclass(kw_only=True)
class PartnerFunctionDetailsResponseDTO(ABBaseDTO):
    partnerFunction: PartnerFunctionDTO = None


@dataclass(kw_only=True)
class IntegrationAutomationListResponseDTO(ABBaseDTO):
    integrationAutomations: list[IntegrationAutomationDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class IntegrationAutomationDetailsResponseDTO(ABBaseDTO):
    integrationAutomation: IntegrationAutomationDTO = None


@dataclass(kw_only=True)
class IntegrationConnectionListResponseDTO(ABBaseDTO):
    integrationConnection: list[IntegrationConnectionDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class IntegrationConnectionResponseDataDTO(ABBaseDTO):
    integrationConnection: IntegrationConnectionDTO = None


@dataclass(kw_only=True)
class IntegrationConnectionCreateResponseDTO(ABBaseDTO):
    integration: IntegrationConnectionResponseDataDTO = None


@dataclass(kw_only=True)
class IntegrationConnectionGetResponseDTO(ABBaseDTO):
    integrationConnection: IntegrationConnectionDTO = None


@dataclass(kw_only=True)
class FieldMappedPropertiesDTO(ABBaseDTO):
    name: str = None
    value: str = None


@dataclass(kw_only=True)
class IntegrationPaginationDTO(ABBaseDTO):
    resultCount: int = None
    limit: int = None
    offset: int = None
    hasMore: str = None
    nextOffset: str = None



@dataclass(kw_only=True)
class LinkedAccountDTO(ABBaseDTO):
    name: str = None
    status: str = None
    id: str = None
    uuid: str = None
    type: str = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    fieldMappedProperties: list = None #[FieldMappedPropertiesDTO]
    projectId: str = None
    projectName: str = None
    projectNumber: str = None
    projectRefNo: str = None
    projectDescription: str = None
    projectType: str = None
    projectStartDate: str = None
    projectEndDate: str = None
    projectStatus: str = None
    projectSubStatus: str = None
    projectLocation: str = None
    projectContact: str = None
    projectManager: str = None
    projectOwner: str = None
    associatedClientName: str = None

@dataclass(kw_only=True)
class LinkedCustomerDTO(ABBaseDTO):
    name: str = None
    status: str = None
    id: str = None
    uuid: str = None
    type: str = None
    createdBy: str = None
    createdOn: str = None
    lastUpdatedBy: str = None
    lastUpdatedOn: str = None
    fieldMappedProperties: list = None #[FieldMappedPropertiesDTO]
    clientId: str = None
    clientName: str = None
    clientNumber: str = None
    clientRefNo: str = None
    clientDescription: str = None
    clientType: str = None
    clientStartDate: str = None
    clientEndDate: str = None
    clientStatus: str = None
    clientSubStatus: str = None
    clientLocation: str = None
    clientContact: str = None
    clientManager: str = None
    clientOwner: str = None
    associatedClientName: str = None


@dataclass(kw_only=True)
class LinkedAccountsResponseDTO(ABBaseDTO):
    linkedAccounts: list[LinkedAccountDTO] = None
    pagination: IntegrationPaginationDTO = None


@dataclass(kw_only=True)
class LinkedAccountResponseDTO(ABBaseDTO):
    linkedAccount: LinkedAccountDTO = None


@dataclass(kw_only=True)
class LinkedCustomersListResponseDTO(ABBaseDTO):
    linkedCustomers: list[LinkedCustomerDTO] = None
    pagination: IntegrationPaginationDTO = None


@dataclass(kw_only=True)
class LinkedCustomersDetailsResponseDTO(ABBaseDTO):
    linkedCustomer: LinkedCustomerDTO = None


@dataclass(kw_only=True)
class PartnerFunctionDTO(ABBaseDTO):
    uuid: str = None
    name: str = None
    description: str = None
    direction: str = None
    eventName: str = None
    providerName: str = None
    objectName: str = None
    objectMapping: str = None
    mappingId: str = None
    enabled: str = None
    preRunScriptId: str = None
    postRunScriptId: str = None
    tag: str = None
    created: str = None
    updated: str = None


@dataclass(kw_only=True)
class PartnerFunctionRequestDTO(ABBaseDTO):
    partnerFunction: PartnerFunctionDTO() = None


@dataclass(kw_only=True)
class PartnerFunctionCreateResponseDTO(ABBaseDTO):
    partnerFunction: PartnerFunctionDTO = None


@dataclass(kw_only=True)
class PartnerFunctionUpdateResponseDTO(ABBaseDTO):
    uuid: str = None
    name: str = None
    description: str = None
    direction: str = None
    eventName: str = None
    providerName: str = None
    objectName: str = None
    objectMapping: str = None
    mappingId: str = None
    enabled: str = None
    preRunScriptId: str = None
    postRunScriptId: str = None
    tag: str = None
    created: str = None
    updated: str = None


@dataclass(kw_only=True)
class PartnerFunctionEnableResponseDTO(ABBaseDTO):
    message: str = None


@dataclass(kw_only=True)
class PartnerFunctionDisableResponseDTO(ABBaseDTO):
    message: str = None


@dataclass(kw_only=True)
class IntegrationAutomationDTO(ABBaseDTO):
    checkOn: str = None
    checkOnMinutes: str = None
    additionalCriteria: str = None
    appliesTo: str = None
    appliesToFunction: str = None
    automationType: str = None
    code: str = None
    customDay: str = None
    customDayTime: str = None
    customTime: str = None
    description: str = None
    direction: str = None
    displayName: str = None
    name: str = None
    performFunction: str = None
    provider: str = None
    status: str = None
    uuid: str = None
    triggerConditionText: str = None
    performActionText: str = None
    checkOnText: str = None


@dataclass(kw_only=True)
class AutomationDetailsDTO(ABBaseDTO):
    name: str = None
    displayName: str = None
    code: str = None
    descriptionEnabled: str = None
    description: str = None
    anotherAutomation: str = None
    appliesTo: str = None
    appliesToFunction: str = None
    automationType: str = None
    direction: str = None
    checkOn: str = None
    customDay: str = None
    customTime: str = None
    doNotOverWriteLatestData: str = None
    ignoreThreshold: str = None
    performAction: str = None
    sinceLastLookUp: str = None
    additionalCriteria: str = None
    propertyName: str = None


@dataclass(kw_only=True)
class CriteriaRuleDTO(ABBaseDTO):
    fieldName: str = None
    operator: str = None
    value: str = None
    condition: str = None


@dataclass(kw_only=True)
class AdditionalCriteriaDTO(ABBaseDTO):
    groupCondition: str = None
    rules: list[CriteriaRuleDTO] = None


@dataclass(kw_only=True)
class IntegrationDTO(ABBaseDTO):
    automationDetails: AutomationDetailsDTO = None
    additionalCriteriaDetails: list[AdditionalCriteriaDTO] = None


@dataclass(kw_only=True)
class AutomationRequestDTO(ABBaseDTO):
    integration: IntegrationDTO = None


@dataclass(kw_only=True)
class AutomationUpdateResponseDTO(ABBaseDTO):
    integrationAutomation: IntegrationAutomationDTO = None


@dataclass(kw_only=True)
class MappingDTO(ABBaseDTO):
    source: str = None
    target: str = None


@dataclass(kw_only=True)
class AccountMappingDTO(ABBaseDTO):
    enabled: str = None
    mappings: list[MappingDTO] = None


@dataclass(kw_only=True)
class AccountImportExportDTO(ABBaseDTO):
    enabled: str = None
    defaultAccountReceivable: str = None
    accountReceivableMapping: AccountMappingDTO = None
    defaultAccountPayable: str = None
    accountPayableMapping: AccountMappingDTO = None
    defaultTax: str = None
    taxMapping: AccountMappingDTO = None
    xeroAccountNumberField: str = None
    xeroAccountIdField: str = None
    syncToXero: str = None


@dataclass(kw_only=True)
class AccountDTO(ABBaseDTO):
    export: AccountImportExportDTO = None
    import_: AccountImportExportDTO = None

    _custom_field_mapping = {
        "import": "import_"
    }


@dataclass(kw_only=True)
class SalesRevenueMappingDTO(ABBaseDTO):
    enabled: str = None
    mappings: list[MappingDTO] = None


@dataclass(kw_only=True)
class InvoiceExportDTO(ABBaseDTO):
    enabled: str = None
    defaultSalesRevenue: str = None
    salesRevenueMapping: SalesRevenueMappingDTO = None
    xeroInvoiceNumberField: str = None
    syncToXero: str = None


@dataclass(kw_only=True)
class InvoiceDTO(ABBaseDTO):
    export: InvoiceExportDTO = None


@dataclass(kw_only=True)
class TransactionDTO(ABBaseDTO):
    invoice: InvoiceDTO = None


@dataclass(kw_only=True)
class IntegrationConnectionConfigRequestDTO(ABBaseDTO):
    account: AccountDTO = None
    transaction: TransactionDTO = None

    _custom_field_mapping = {
        "import": "import_"
    }


@dataclass(kw_only=True)
class IntegrationConnectionConfigResponseDTO(ABBaseDTO):
    message: str = None


@dataclass(kw_only=True)
class IntegrationAutomationDTO(ABBaseDTO):
    checkOn: str = None
    checkOnMinutes: str = None
    additionalCriteria: str = None
    appliesTo: str = None
    appliesToFunction: str = None
    automationType: str = None
    code: str = None
    customDay: str = None
    customDayTime: str = None
    customTime: str = None
    description: str = None
    direction: str = None
    displayName: str = None
    name: str = None
    performFunction: str = None
    provider: str = None
    status: str = None
    uuid: str = None
    triggerConditionText: str = None
    performActionText: str = None
    checkOnText: str = None


@dataclass(kw_only=True)
class AutomationDetailsDTO(ABBaseDTO):
    name: str = None
    displayName: str = None
    code: str = None
    descriptionEnabled: str = None
    description: str = None
    anotherAutomation: str = None
    appliesTo: str = None
    appliesToFunction: str = None
    automationType: str = None
    direction: str = None
    checkOn: str = None
    customDay: str = None
    customTime: str = None
    doNotOverWriteLatestData: str = None
    ignoreThreshold: str = None
    performAction: str = None
    sinceLastLookUp: str = None
    additionalCriteria: str = None
    propertyName: str = None


@dataclass(kw_only=True)
class CriteriaRuleDTO(ABBaseDTO):
    fieldName: str = None
    operator: str = None
    value: str = None
    condition: str = None


@dataclass(kw_only=True)
class AdditionalCriteriaDTO(ABBaseDTO):
    groupCondition: str = None
    rules: list[CriteriaRuleDTO] = None


@dataclass(kw_only=True)
class IntegrationDTO(ABBaseDTO):
    automationDetails: AutomationDetailsDTO = None
    additionalCriteriaDetails: list[AdditionalCriteriaDTO] = None


@dataclass(kw_only=True)
class AutomationRequestDTO(ABBaseDTO):
    integration: IntegrationDTO = None


@dataclass(kw_only=True)
class AutomationCreateResponseDTO(ABBaseDTO):
    integrationAutomation: IntegrationAutomationDTO = None
