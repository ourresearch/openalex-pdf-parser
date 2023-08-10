class APIError(Exception):
    """All custom API Exceptions"""
    code = None
    description = None

    pass


class S3FileNotFoundError(APIError):
    """Error when file does not exist in S3."""

    code = 404
    description = "Source file not found on S3. Nothing to parse."


class WrongFormatLandingPageError(APIError):

    def __init__(self, format_):
        self.format_ = format_
        self.description = f'Wrong format landing page ({self.format_} format). Unable to parse.'

    code = 400
