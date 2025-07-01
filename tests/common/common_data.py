from exsited.exsited.auth.dto.token_dto import RequestTokenDTO


class CommonData:

    @staticmethod
    def get_request_token_dto():
        return RequestTokenDTO(
            grantType="client_credentials",
            clientId="YC42NmBgMWMrMzVjMS8yOTArNGFkNisyNDIzK18xZGErYi8wMDBjNzM1MDIzKzcuLjArNGE2YS4=",
            clientSecret="YjA4OGJiM2UtZTAxNTY3MjMtYmIzMS00YjRkLWExMGEtYjk1Njc1N2M4MWVmLTkwMDItYmI0ZjE=",
            redirectUri="https://www.google.com/",
            exsitedUrl="https://dev-api.exsited.com/",
        )
