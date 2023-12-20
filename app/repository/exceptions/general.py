class NotFoundException(Exception):
    """Exception raised when an entity is not found."""
    pass

class DatabaseException(Exception):
    """Generic exception for database related errors."""
    pass