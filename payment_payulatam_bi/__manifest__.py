# -*- coding: utf-8 -*-
# Part of  See LICENSE file for full copyright and licensing details.
##############################################################################
{
    'name': 'Website Payu Payment Acquire',
    'author':'',
    'category': 'eCommerce',
    'website' : "",
    'summary': '',
    'version': '12.0.0.1',
    'description': """Payu Payment Acquirer
		Website PayuLatam Payment Acquirer integration with Odoo shop
		Website Payment Acquirer PayuLatam
		Website Latin Europe payment gateway with odoo
		Website Latin Europe payment Acquirer
		Website Payu Payment Acquirer
		Website payment payu Acquirer


		Website Payu Latam Payment Acquirer integration with Odoo shop
		Website Payment Acquirer Payu Latam
		Website Pay u Payment Acquirer
		Website payment pay u Acquirer

		Website Payu Payment Acquirer integration with Odoo shop
		Website Payment Acquirer Payu
		Website Pay-u Payment Acquirer
		Website payment pay-u Acquirer


""",
    'depends': ['payment','website_sale'],
    "price": 49,
    "currency": 'EUR',
    'data': [
        'views/payment_acquirer.xml',
        'views/payment_payu_template.xml',
        'data/payu.xml',
    ],
    'installable': True,
    "images":["static/description/Banner.png"],
}
