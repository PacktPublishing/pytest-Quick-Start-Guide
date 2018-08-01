from . import testing


class Test(testing.DataBaseTesting):

    def test1(self):
        self.create_table("weapons", name=str, type=str, dmg=int)
        ...
