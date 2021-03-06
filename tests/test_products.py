import unittest
from datahub.products import Products


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.id = 7

    def test_get_product(self):
        id = 7
        p = Products()
        product = p.get(id)
        self.assertEqual(id, product["id"])

    def test_get_product_invalid_id(self):
        id = -5
        p = Products()
        product = p.get(id)
        self.assertIsNone(product)

    def test_get_product_by_name(self):
        name = "GLOBAL_REANALYSIS_PHY_001_030"
        p = Products()
        product = p.get_by_name_alias(name)
        self.assertIsNotNone(product)

    def test_get_product_by_name_ko(self):
        name = "FAKE_GLOBAL_REANALYSIS_PHY_001_030"
        p = Products()
        product = p.get_by_name_alias(name)
        self.assertIsNone(product)

    def test_get_product_by_alias(self):
        alias = "GLOBAL REANALYSIS PHY 001 030"
        p = Products()
        product = p.get_by_name_alias(alias)
        self.assertIsNotNone(product)

    def test_get_product_by_alias_ko(self):
        alias = "FAKE GLOBAL REANALYSIS PHY 001 030"
        p = Products()
        product = p.get_by_name_alias(alias)
        self.assertIsNone(product)

    def test_get_all(self):
        expected_result = 173
        p = Products()
        all_products = p.get_all()
        n = len(all_products)

        self.assertEqual(n, expected_result)

    def test_get_all_filter(self):
        expected_result = 121
        p = Products()
        all_products = p.get_all(lon_min=-10, lon_max=0, lat_min=40, lat_max=50)
        n = len(all_products)

        self.assertEqual(n, expected_result)

    def test_get_all_filter_partial(self):
        p = Products()
        with self.assertRaises(Exception):
            p.get_all(lon_min=-10, lon_max=0, lat_max=50)

    def test_get_variables(self):
        p = Products()
        product = p.get(self.id)
        variables = p.get_variables(product)
        n = len(variables)
        self.assertEqual(n, 5)

    def test_get_variables_no_product(self):
        invalid_product = {}
        p = Products()
        with self.assertRaises(Exception):
            p.get_variables(invalid_product)


if __name__ == "__main__":
    unittest.main()
