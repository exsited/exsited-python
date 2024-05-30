from ab_py.autobill.auth.dto.token_dto import RequestTokenDTO


class CommonData:

    @staticmethod
    def get_request_token_dto():
        return RequestTokenDTO(
            # grantType="client_credentials",
            # clientId="NC5hYjFfMV0pLTVfYDVeMjkpXl0xMikwMDEzKTUxLzApM15iMzI0YC0tM11dKTUsLDQpM18zXzM=",
            # clientSecret="LylcXSxaLFgkWGVcWltYMTgkWFhZYyQrMFosJC8nWVwkXCovXCgqKTBcXFgnJDAnJy8kWVknWy4=",
            # redirectUri="https://banglafighter.com",
            # autoBillUrl="https://api-stage.exsited.com",

            grantType="client_credentials",
            clientId="PQsJCgs8PD4GDzg/EgwQYTQGDBI8MgYNCQsQBhIOCz0GOw8/PA4MPTwQPzwLBhIKCwkGOzw7Egw=",
            clientSecret="YjAuLzBhYWMrZDRgMjNfZmErNjE1MSsyNjNiKzYxYDErNDM0LzQvYjJhNjQxKzcvMC4rYTFfX2M=",
            redirectUri="https://www.google.com",
            autoBillUrl="http://localhost:9000",
        )
