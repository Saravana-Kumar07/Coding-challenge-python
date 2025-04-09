class Claim:
    def __init__(self, claimId=0, claimNumber="", dateFiled=None, claimAmount=0.0, status="", policyId=0, clientId=0):
        self.claimId = claimId
        self.claimNumber = claimNumber
        self.dateFiled = dateFiled
        self.claimAmount = claimAmount
        self.status = status
        self.policyId = policyId
        self.clientId = clientId

    def __str__(self):
        return (f"Claim [ID: {self.claimId}, Number: {self.claimNumber}, Date: {self.dateFiled}, Amount: {self.claimAmount}, "
                f"Status: {self.status}, Policy ID: {self.policyId}, Client ID: {self.clientId}]")
