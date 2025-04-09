class PolicyNotFoundException(Exception):
    def __init__(self, message="Policy not found."):
        super().__init__(message)


class DatabaseConnectionException(Exception):
    def __init__(self, message="Error connecting to the database."):
        super().__init__(message)


class InvalidInputException(Exception):
    def __init__(self, message="Invalid input provided."):
        super().__init__(message)
