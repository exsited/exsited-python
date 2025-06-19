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
class IntegrationConnectionListResponseDTO(ABBaseDTO):
    integrationConnection: list[IntegrationConnectionDTO] = None


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
    quotedMargin: str = None
    lifeSupport: str = None
    nmiNumber: str = None


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
    manager: str = None
    fieldMappedProperties: FieldMappedPropertiesDTO = None
    ekoProjectName: str = None
    ekoProjectId: str = None
    ekoProjectStatus: str = None
    ekoProjectSubStatus: str = None


@dataclass(kw_only=True)
class LinkedAccountsResponseDTO(ABBaseDTO):
    linkedAccounts: list[LinkedAccountDTO] = None
    pagination: PaginationDTO = None


@dataclass(kw_only=True)
class LinkedAccountResponseDTO(ABBaseDTO):
    linkedAccount: LinkedAccountDTO = None


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
