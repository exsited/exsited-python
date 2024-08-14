from ab_py.exsited.auth.dto.token_dto import RequestTokenDTO


class CommonData:

    @staticmethod
    def get_request_token_dto():
        return RequestTokenDTO(
            grantType="",
            clientId="",
            clientSecret="",
            redirectUri="",
            exsitedUrl="",
        )
