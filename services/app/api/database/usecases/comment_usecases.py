import dataclasses
from typing import Any, Optional

from flask import jsonify

from ...exceptions.exceptions import ResourceExistsException
from ..models.comment_model import Comment
from ..repositories.unit_of_work import BaseUnitfWork
from .querie_mixin import QueryMixin
from .use_case import UseCase


class AddCommentUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment = Comment(
                video_id=data['video_id'],
                comment_id=data['comment_id'],
                comment_text=data['comment_text'],
                parent_id=data['parent_id'],
                like_count=data['like_count'],
                published_at=data['published_at'],
                updated_at=data['updated_at'],
            )
            uow.repository.add(comment)
        return dataclasses.asdict(comment)


class GetCommentUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_id = data['id']
            comment = uow.repository.get_by_id(comment_id)
        return dataclasses.asdict(comment)


class DeleteCommentUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_id = data['id']
            comment = uow.repository.get_by_id(comment_id)
            uow.repository.delete(comment_id)
        return dataclasses.asdict(comment)


class UpdateCommentUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_id = data['id']
            comment = uow.repository.get_by_id(comment_id)
            if data.get('video_id'):
                comment.video_id = data.get('video_id')
            if data.get('comment_id'):
                comment.comment_id = data.get('comment_id')
            if data.get('comment_text'):
                comment.comment_text = data.get('comment_text')
            if data.get('parent_id'):
                comment.parent_id = data.get('parent_id')
            if data.get('like_count'):
                comment.like_count = data.get('like_count')
            if data.get('published_at'):
                comment.published_at = data.get('published_at')
            if data.get('updated_at'):
                comment.updated_at = data.get('updated_at')
            uow.repository.update(comment)
        return dataclasses.asdict(comment)


class GetCommentsUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            sort_field = 'id'
            limit = 10
            offset = 0
            sort_order = 'ASC'
            if data.get('sort_field'):
                sort_field = data.get('sort_field')
            if data.get('limit'):
                limit = data.get('limit')
            if data.get('offset'):
                offset = data.get('offset')
            if data.get('sort_order'):
                sort_order = data.get('sort_order')
            comments = uow.repository.list_all(sort_field=sort_field, limit=limit, offset=offset, sort_order=sort_order)
        return jsonify(comments)


class AddManyCommentsUseCase(UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        with self.unit_of_work as uow:
            comment_data_list: list[dict[str, str | int]] = data['comments']
            comments_added: int = 0
            for data in comment_data_list:
                comment = Comment(
                    video_id=data['video_id'],
                    comment_id=data['comment_id'],
                    comment_text=data['comment_text'],
                    parent_id=data['parent_id'],
                    like_count=data['like_count'],
                    published_at=data['published_at'],
                    updated_at=data['updated_at'],
                )
                try:
                    uow.repository.add(comment)
                    comments_added += 1
                except ResourceExistsException:
                    pass
        return {'Comments Added': comments_added}


# TODO
class QueryCommentUseCase(QueryMixin, UseCase):
    def __init__(self, unit_of_work: Optional[BaseUnitfWork] = None) -> None:
        super().__init__(unit_of_work)

    def execute(self, data: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError()
