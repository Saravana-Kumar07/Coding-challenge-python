class Client:
    def __init__(self, clientId=0, clientName="", contactInfo="", policyId=0):
        self.clientId = clientId
        self.clientName = clientName
        self.contactInfo = contactInfo
        self.policyId = policyId

    def __str__(self):
        return f"Client [ID: {self.clientId}, Name: {self.clientName}, Contact: {self.contactInfo}, Policy ID: {self.policyId}]"
