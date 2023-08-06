class ShippingContainer:

    next_serial = 1337

    def _generate_serial(self):
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self._generate_serial()