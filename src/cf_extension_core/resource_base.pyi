from _typeshed import Incomplete
from cf_extension_core.dynamo_table_creator import DynamoTableCreator as DynamoTableCreator
from cloudformation_cli_python_lib.interface import BaseResourceHandlerRequest as _BaseResourceHandlerRequest
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource, Table
from typing import Any, Optional, Type, TYPE_CHECKING

logger: Incomplete

class ResourceBase:
    T: Incomplete
    _request: Incomplete
    _db_resource: Incomplete
    _primary_identifier: Incomplete
    _type_name: Incomplete
    def __init__(
        self,
        db_resource: DynamoDBServiceResource,
        request: _BaseResourceHandlerRequest,
        type_name: str,
        primary_identifier: Optional[str] = ...,
    ) -> None: ...

    class _ResourceData:
        _HELPER_KEY: str
        T: Incomplete
        @staticmethod
        def _model_to_string(model: T) -> str: ...
        @staticmethod
        def _model_from_string(modelstr: str, class_type: Type[T]) -> T: ...

        class DecryptionException(Exception):
            def __init__(self, *args: Any) -> None: ...

    def _current_time(self) -> str: ...
    def _get_primary_identifier(self) -> str: ...
    def _not_found_check(self) -> None: ...
    def _dynamo_db_table(self) -> Table: ...
    def _db_item_insert_without_overwrite(self, model: T) -> None: ...
    def _db_item_update_model(self, model: T) -> None: ...
    def _db_get_item(self) -> Any: ...
    def _db_item_exists(self) -> bool: ...
    def _db_item_get_model(self, model_type: Type[T]) -> T: ...
    def _db_item_list_primary_identifiers_for_cr_type(self) -> list[str]: ...
    def _db_item_delete(self, best_effort: bool = ...) -> None: ...
