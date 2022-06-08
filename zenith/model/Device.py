class Device:
    def __init__(self, td, name, status, postCode, type):
        self.td = td
        self.name = name
        self.status = status
        self.postCode = postCode
        self.type = type

class DeviceList:
    def __init__(self, result, message, uid, data):
        self.result = result
        self.message = message
        self.uid = uid
        self.data = data

    def __str__(self):
        return "result={}, message={}".format(self.result, self.message)
