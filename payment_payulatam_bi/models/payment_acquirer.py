# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
##############################################################################
from werkzeug import urls
import hashlib

from odoo.addons.payment_payu.controllers.main import PayuLatamController

from odoo import api, fields, models, _
from odoo.exceptions import except_orm, Warning, RedirectWarning


class PaymentAcquirerPayu(models.Model):
    _inherit = 'payment.acquirer'

    def _get_payu_urls(self, environment):
        """ Payu URLs
        """
        if environment == 'prod':
            return {'payu_form_url': 'https://secure.payu.com/api/v2_1/orders'}
        else:
            return {'payu_form_url': 'https://secure.snd.payu.com/api/v2_1/orders'}

    @api.model
    def _get_providers(self):
        providers = super(PaymentAcquirerPayu, self)._get_providers()
        providers.append(['payu', 'Payu'])
        return providers

    provider = fields.Selection(selection_add=[('payu', 'Payu')])
    payu_merchantId = fields.Char(string='Merchant ID', required_if_provider='payu')
    payu_accountId = fields.Char(string='Account ID', required_if_provider='payu')
    payu_apiKey = fields.Char(string='API Key', required_if_provider='payu')

    def _payu_generate_hashing(self, values):
        data = '~'.join([
            values['ApiKey'],
            values['merchantId'],
            values['referenceCode'],
            values['amount'],
            values['currency']])
        m = hashlib.md5()
        m.update(data.encode("utf-8"))
        return m.hexdigest()

    @api.multi
    def payu_form_generate_values(self, values):
        payu_tx_values = dict(values)
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        if self.environment == 'prod':
            test = 0
        else:
            test = 1
        temp_paylatam_tx_values = dict(
            ApiKey=self.payu_apiKey,
            merchantId=self.payu_merchantId,
            accountId=self.payu_accountId,
            referenceCode=values['reference'],
            description=values['reference'],
            amount=str(values['amount']),
            tax=0,
            currency=values['currency'] and values['currency'].name or '',
            currency_sel=['CZK', 'EUR', 'USD'],
            taxReturnBase=0,
            buyerEmail=values['partner_email'],
            test=test,
            responseUrl='%s' % urls.url_join(
                base_url, PayuController._return_url),
        )
        temp_pay_tx_values['signature'] = self._payu_generate_hashing(temp_pay_tx_values)
        payu_tx_values.update(temp_pay_tx_values)
        return payu_tx_values

    @api.multi
    def payu_get_form_action_url(self):
        self.ensure_one()
        return self._get_payu_urls(self.environment)['payu_form_url']

PaymentAcquirerPayu()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
