class VideoExistsException(Exception):
    """Raised when an existing video is added to the Repository."""
    
class VideoDoesNotExistException(Exception):
    """Raised when a video does not exist in the repository."""