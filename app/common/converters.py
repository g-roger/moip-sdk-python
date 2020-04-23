import re
from functools import partial

from marshmallow import Schema

snake_case = re.compile(r"(?<=\w)_(\w)")
camel_case = partial(snake_case.sub, lambda m: m[1].upper())


class CamelCasedSchema(Schema):
    def on_bind_field(self, field_name, field_obj, _cc=camel_case):
        field_obj.data_key = _cc(field_name.lower())
