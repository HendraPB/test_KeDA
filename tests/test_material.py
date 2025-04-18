from odoo.tests.common import TransactionCase

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['res.partner'].create({
            'name': 'Unit Test Supplier'
        })

    def test_create_material_valid(self):
        material = self.env['keda.material'].create({
            'code': 'CTN999',
            'name': 'Cotton unit test 999',
            'type': 'cotton',
            'buy_price': 150,
            'supplier_id': self.supplier.id
        })
        self.assertTrue(material.id)

    def test_create_material_invalid_price(self):
        with self.assertRaises(Exception):
            self.env['keda.material'].create({
                'code': 'JNS999',
                'name': 'Jeans unit test 999',
                'type': 'jeans',
                'buy_price': 50,
                'supplier_id': self.supplier.id
            })