from marshmallow import fields

from app.common.converters import CamelCasedSchema


class CustomerSchema(CamelCasedSchema):
    own_id = fields.Integer(required=True)
    fullname = fields.String(required=True)
    email = fields.Email(required=True)
    birth_date = fields.Date(required=True)
    tax_document = fields.Nested('TaxDocumentSchema', required=True)
    phone = fields.Nested('PhoneSchema', required=True)
    shipping_address = fields.Nested('ShippingAddressSchema')


class ShippingAddressSchema(CamelCasedSchema):
    city = fields.String()
    district = fields.String()
    street = fields.String()
    street_number = fields.String()
    zip_code = fields.String()
    state = fields.String()
    country = fields.String()


class TaxDocumentSchema(CamelCasedSchema):
    type = fields.String(required=True)
    number = fields.String(required=True)


class PhoneSchema(CamelCasedSchema):
    country_code = fields.String(required=True)
    area_code = fields.String(required=True)
    number = fields.String(required=True)
