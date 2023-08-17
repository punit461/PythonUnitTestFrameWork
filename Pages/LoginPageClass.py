# from Utilities import BaseClass
from Utilities.Base import BaseClass


class LoginPageClass(BaseClass):

    def test(self):
        timeout = self.timeout()
        print(timeout)


LoginPageClass.test()
