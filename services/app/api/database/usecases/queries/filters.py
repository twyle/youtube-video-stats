from typing import Any, Optional

from .filter import Filter

q = {"comments_count": {"eq": 100}}


class EqualFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'eq' operator is used
            if field_parameters.get("eq"):
                fields_to_drop.append(field_name)
                operator = self.operator_map["eq"]
                value = field_parameters.get("eq")
                if "WHERE" in query:
                    query = query + f" AND {field_name} {operator} {value}"
                else:
                    query = query + f" WHERE {field_name} {operator} {value}"
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters


class GreaterThanFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'gt' operator is used
            if field_parameters.get("gt"):
                fields_to_drop.append(field_name)
                operator = self.operator_map["gt"]
                value = field_parameters.get("gt")
                if "WHERE" in query:
                    query = query + f" AND {field_name} {operator} {value}"
                else:
                    query = query + f" WHERE {field_name} {operator} {value}"
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters


class GreaterThanEqualToFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'gte' operator is used
            if field_parameters.get("gte"):
                fields_to_drop.append(field_name)
                operator = self.operator_map["gte"]
                value = field_parameters.get("gte")
                if "WHERE" in query:
                    query = query + f" AND {field_name} {operator} {value}"
                else:
                    query = query + f" WHERE {field_name} {operator} {value}"
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters


class LessThanFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'lt' operator is used
            if field_parameters.get("lt"):
                fields_to_drop.append(field_name)
                operator = self.operator_map["lt"]
                value = field_parameters.get("lt")
                if "WHERE" in query:
                    query = query + f" AND {field_name} {operator} {value}"
                else:
                    query = query + f" WHERE {field_name} {operator} {value}"
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters


class LessThanEqualToFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'lte' operator is used
            if field_parameters.get("lte"):
                fields_to_drop.append(field_name)
                operator = self.operator_map["lte"]
                value = field_parameters.get("lte")
                if "WHERE" in query:
                    query = query + f" AND {field_name} {operator} {value}"
                else:
                    query = query + f" WHERE {field_name} {operator} {value}"
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters


class BetweenFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'lte' operator is used
            if field_parameters.get("lte") and field_parameters.get("gte"):
                fields_to_drop.append(field_name)
                gte_value = field_parameters.get("gte")
                lte_value = field_parameters.get("lte")
                if "WHERE" in query:
                    query = query + f" AND {field_name} BETWEEN {gte_value} AND {lte_value}"
                else:
                    query = query + f" WHERE {field_name} BETWEEN {gte_value} AND {lte_value}"
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters


class LessThanGreaterThanFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'lt' and 'gt' operator is used
            if field_parameters.get("lt") and field_parameters.get("gt"):
                fields_to_drop.append(field_name)
                gt_operator = self.operator_map["gt"]
                lt_operator = self.operator_map["lt"]
                gt_value = field_parameters.get("gt")
                lt_value = field_parameters.get("lt")
                if "WHERE" in query:
                    query = (
                        query + f" AND {field_name} {gt_operator} {gt_value} AND {field_name} {lt_operator} {lt_value}"
                    )
                else:
                    query = (
                        query
                        + f" WHERE {field_name} {gt_operator} {gt_value} AND {field_name} {lt_operator} {lt_value}"
                    )
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters


class InFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'lte' operator is used
            if field_parameters.get("in"):
                fields_to_drop.append(field_name)
                operator = self.operator_map["in"]
                value = tuple(field_parameters.get("in"))
                if "WHERE" in query:
                    query = query + f" AND {field_name} {operator} {value}"
                else:
                    query = query + f" WHERE {field_name} {operator} {value}"
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters


class NotInFilter(Filter):
    def __init__(self, next_filter: Optional[Filter] = None) -> None:
        super().__init__(next_filter=next_filter)

    def __call__(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        updated_query, remaining_q_params = self.__filter(query, query_parameters)
        if self.next_filter:
            return self.next_filter(updated_query, remaining_q_params)
        return updated_query, remaining_q_params

    def __filter(
        self, query: str, query_parameters: dict[str, dict[str, Any]]
    ) -> tuple[str, dict[str, dict[str, Any]]]:
        fields_to_drop: list[str] = []
        for field_name, field_parameters in query_parameters.items():
            # Check if 'lte' operator is used
            if field_parameters.get("not in"):
                fields_to_drop.append(field_name)
                operator = self.operator_map["not in"]
                value = tuple(field_parameters.get("not in"))
                if "WHERE" in query:
                    query = query + f" AND {field_name} {operator} {value}"
                else:
                    query = query + f" WHERE {field_name} {operator} {value}"
        for field in fields_to_drop:
            query_parameters.pop(field)
        return query, query_parameters
