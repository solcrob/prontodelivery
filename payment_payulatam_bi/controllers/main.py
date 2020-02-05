# -*- coding: utf-8 -*-
# Part of  See LICENSE file for full copyright and licensing details.
##############################################################################
import logging
import pprint
import werkzeug

from werkzeug import urls

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class PayuController(http.Controller):
    _cancel_url = '/payment/payu/cancel'
    _exception_url = '/payment/payu/error'
    _return_url = '/payment/payu/return'

    @http.route([_return_url, _cancel_url, _exception_url], type='http', auth='public', csrf=False)
    def payu_return(self, **post):
        """ Payu ."""
        _logger.info(
            'Payu: entering form_feedback with post data %s', pprint.pformat(post))
        if post:
            request.env['payment.transaction'].sudo().form_feedback(
                post, 'payu')
        base_url = request.env['ir.config_parameter'].get_param('web.base.url')
        return_url = '%s' % urls.url_join(
                base_url, '/shop/payment/validate')
        return werkzeug.utils.redirect(return_url)
