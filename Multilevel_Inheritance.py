class ElectronicDevice:

    basic='Electronic Device'

    def __init__(self, Type):
        self.type = Type

    def details(self):
        return f'Device is of type: {self.type}'


class PocketGadget(ElectronicDevice):

    def __init__(self, Size):
        self.size = Size

    def sizedetails(self):
        return f' Device is of {self.size} size'


class Mobile(PocketGadget):

    def __init__(self,Name):
        self.name=Name

    def mobiletype(self):
        return f'Mobile is{self.name}'


camera=ElectronicDevice('Photo taking Device')

pager= PocketGadget('Big')

nokia=Mobile('Lumia 520')

print(nokia.mobiletype())

print(pager.sizedetails())

print(camera.details())

print(nokia.basic)