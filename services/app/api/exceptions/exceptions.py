class ResourceExistsException(Exception):
    """Raised when an existing resource is added to the Repository."""


class ResourceNotExistException(Exception):
    """Raised when a resource being fetched does not exist in the repository."""


class VideoExistsException(Exception):
    """Raised when an existing video is added to the Repository."""


class VideoDoesNotExistException(Exception):
    """Raised when a video does not exist in the repository."""


class UserExistsException(Exception):
    """Raised when an existing user is added to the repository."""


class UserDoesNotExistException(Exception):
    """Raised when trying to retrieve a non-existing user from the repository."""
