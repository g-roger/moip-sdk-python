from marshmallow import fields

from moip_sdk.common.converters import CamelCasedSchema


class OrderSchema(CamelCasedSchema):
    own_id = fields.Integer(required=True)
    amount = fields.Nested('AmountSchema')
    items = fields.Nested('ItemsSchema', many=True, required=True)
    customer = fields.Nested('CustomerIdSchema', required=True)


class AmountSchema(CamelCasedSchema):
    currency = fields.String(required=True)
    subtotals = fields.Nested('SubtotalsSchema')


class SubtotalsSchema(CamelCasedSchema):
    shipping = fields.Integer()
    addition = fields.Integer()
    discount = fields.Integer()
    items = fields.Integer()


class ItemsSchema(CamelCasedSchema):
    product = fields.String(required=True)
    category = fields.String()
    quantity = fields.Integer(required=True)
    detail = fields.String()
    price = fields.Integer(required=True)


class CustomerIdSchema(CamelCasedSchema):
    id = fields.String(required=True)
