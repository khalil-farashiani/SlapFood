class RestError:
    external_status_code : int
    internal_status_code : int
    error_message : str

    def __init__(self, external_status:int, status:int, error:str) -> None:
        self.external_status_code=external_status
        self.status_code=status
        self.error_message=error