from . import testing


class Test(testing.DataBaseTesting, testing.GUITesting):

    def setUp(self):
        testing.DataBaseTesting.setUp(self)
        testing.GUITesting.setUp(self)

    def tearDown(self):
        testing.GUITesting.setUp(self)
        testing.DataBaseTesting.setUp(self)

    def test1(self):
        assert self.app is not None
        assert self.session is not None
