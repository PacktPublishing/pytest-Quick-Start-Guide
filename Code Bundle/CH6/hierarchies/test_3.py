from . import testing


class Test(testing.DataBaseTesting, testing.GUITesting):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test1(self):
        pass
