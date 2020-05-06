from marshmallow import fields
from marshmallow_enum import EnumField

from moip_sdk.common.converters import CamelCasedSchema
from moip_sdk.payment.enums import MoipPaymentMethod


class PaymentSchema(CamelCasedSchema):
    installment_count = fields.Integer(required=True)
    statement_descriptor = fields.String(required=True)
    funding_instrument = fields.Nested('FundingInstrumentSchema')


class FundingInstrumentSchema(CamelCasedSchema):
    method = EnumField(MoipPaymentMethod, required=True)
    credit_card = fields.Nested('CreditCardSchema')
    boleto = fields.Nested('BoletoSchema')


class CreditCardSchema(CamelCasedSchema):
    hash = fields.String()
    store = fields.Boolean()
    holder = fields.Nested('HolderSchema')


class HolderSchema(CamelCasedSchema):
    fullname = fields.String()
    birth_date = fields.Date()
    tax_document = fields.Nested('TaxDocumentSchema')
    phone = fields.Nested('PhoneSchema')


class InstructionLinesSchema(CamelCasedSchema):
    first = fields.String()
    second = fields.String()
    third = fields.String()


class BoletoSchema(CamelCasedSchema):
    expiration_date = fields.Date()
    instruction_lines = fields.Nested('InstructionLinesSchema')
    logo_uri = fields.String()
