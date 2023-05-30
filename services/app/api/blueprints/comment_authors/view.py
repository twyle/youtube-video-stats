from flask import Blueprint, request
from flasgger import swag_from
from ...controllers.response_builders.create_response import ResponseBuilder
from ...controllers.controllers.user_controller_factory import (
    CreateUserControllerFactory, DeleteUserControllerFactory, ListUsersControllerFactory,
    ActivateAccountControllerFactory, LoginUserControllerFactory, GetUserControllerFactory,
    UpdateUserControllerFactory
)
from ..decorators import admin_token_required
from flask_jwt_extended import jwt_required


comment_authors = Blueprint('comment_authors', __name__)

@swag_from('./docs/register.yml', endpoint='comment_authors.register_client', methods=['POST'])
@comment_authors.route('/register', methods=['POST'])
def register_client():
    controller = CreateUserControllerFactory()
    create_user_builder = ResponseBuilder()
    api_response = (
        create_user_builder.with_data_validators(controller.get_request_data_validator())
        .with_request_builder(controller.get_request_builder())
        .with_request_object(request)
        .with_request_handler(controller.get_request_handler())
        .with_controller(controller.get_controller())
        .build()
    )
    return api_response


@comment_authors.route('/get', methods=['GET'])
@jwt_required()
@swag_from('./docs/get.yml', endpoint='comment_authors.get_client', methods=['GET'])
def get_client(): 
    controller = GetUserControllerFactory()
    create_user_builder = ResponseBuilder()
    api_response = (
        create_user_builder.with_data_validators(controller.get_request_data_validator())
        .with_request_builder(controller.get_request_builder())
        .with_request_object(request)
        .with_request_handler(controller.get_request_handler())
        .with_controller(controller.get_controller())
        .build()
    )
    return api_response


@comment_authors.route('/update', methods=['PUT'])
@jwt_required()
@swag_from('./docs/update.yml', endpoint='comment_authors.update_client', methods=['PUT'])
def update_client():
    controller = UpdateUserControllerFactory()
    create_user_builder = ResponseBuilder()
    api_response = (
        create_user_builder.with_data_validators(controller.get_request_data_validator())
        .with_request_builder(controller.get_request_builder())
        .with_request_object(request)
        .with_request_handler(controller.get_request_handler())
        .with_controller(controller.get_controller())
        .build()
    )
    return api_response


@comment_authors.route('/delete', methods=['DELETE'])
@admin_token_required
@swag_from('./docs/delete.yml', endpoint='comment_authors.delete_client', methods=['DELETE'])
def delete_client():
    controller = DeleteUserControllerFactory()
    create_user_builder = ResponseBuilder()
    api_response = (
        create_user_builder.with_data_validators(controller.get_request_data_validator())
        .with_request_builder(controller.get_request_builder())
        .with_request_object(request)
        .with_request_handler(controller.get_request_handler())
        .with_controller(controller.get_controller())
        .build()
    )
    return api_response


@comment_authors.route('/users', methods=['GET'])
@admin_token_required
@swag_from('./docs/users.yml', endpoint='comment_authors.list_all', methods=['GET'])
def list_all():
    controller = ListUsersControllerFactory()
    response_builder = ResponseBuilder()
    api_response = (
        response_builder.with_data_validators(controller.get_request_data_validator())
        .with_request_builder(controller.get_request_builder())
        .with_request_object(request)
        .with_request_handler(controller.get_request_handler())
        .with_controller(controller.get_controller())
        .build()
    )
    return api_response
    
