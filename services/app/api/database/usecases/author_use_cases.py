import dataclasses
from typing import Any, Optional

from flask import jsonify

from ..models.author_model import CommentAuthor
from ..repositories.unit_of_work import BaseUnitfWork
from .use_case import UseCase


class CreateCommentAuthorUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_author = CommentAuthor(
                author_display_name=data['author_display_name'],
                author_profile_image_url=data['author_profile_image_url'],
                author_channel_url=data['author_channel_url'],
                author_channel_id=data['author_channel_id'],
            )
            uow.repository.add(comment_author)
        return dataclasses.asdict(comment_author)


class GetCommentAuthorUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_author_id = data['comment_author_id']
            comment_author = uow.repository.get_by_id(comment_author_id)
        return dataclasses.asdict(comment_author)


class DeleteCommentAuthorUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_author_id = data['comment_author_id']
            comment_author = uow.repository.get_by_id(comment_author_id)
            uow.repository.delete(comment_author_id)
        return dataclasses.asdict(comment_author)


class UpdateCommentAuthorUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_author_id = data['author_id']
            comment_author = uow.repository.get_by_id(comment_author_id)
            if data.get('author_display_name'):
                comment_author.author_display_name = data.get('author_display_name')
            if data.get('author_profile_image_url'):
                comment_author.author_profile_image_url = data.get('author_profile_image_url')
            if data.get('author_channel_url'):
                comment_author.author_channel_url = data.get('author_channel_url')
            if data.get('author_channel_id'):
                comment_author.author_channel_id = data.get('author_channel_id')
            uow.repository.update(comment_author)
        return dataclasses.asdict(comment_author)


class GetAllCommentAuthorsUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_authors = uow.repository.list_all()
        return jsonify(comment_authors)
