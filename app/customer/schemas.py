from marshmallow import fields

from app.common.converters import CamelCasedSchema


class CustomerSchema(CamelCasedSchema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    birth_date = fields.Date(required=True)
    cpf = fields.String(required=True)
    phone = fields.Nested('PhoneSchema', required=True)
    address = fields.Nested('AddressSchema')


class AddressSchema(CamelCasedSchema):
    city = fields.String()
    district = fields.String()
    street = fields.String()
    street_number = fields.String()
    zip_code = fields.String()
    state = fields.String()
    country = fields.String()


class PhoneSchema(CamelCasedSchema):
    country_code = fields.String(required=True)
    area_code = fields.String(required=True)
    number = fields.String(required=True)
