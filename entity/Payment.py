class Payment:
    def __init__(self, paymentId=0, paymentDate=None, paymentAmount=0.0, clientId=0):
        self.paymentId = paymentId
        self.paymentDate = paymentDate
        self.paymentAmount = paymentAmount
        self.clientId = clientId

    def __str__(self):
        return (f"Payment [ID: {self.paymentId}, Date: {self.paymentDate}, Amount: {self.paymentAmount}, "
                f"Client ID: {self.clientId}]")
