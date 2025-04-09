class Policy:
    def __init__(self, policyId=0, policyName="", premiumAmount=0.0, coverageAmount=0.0, termYears=0):
        self.policyId = policyId
        self.policyName = policyName
        self.premiumAmount = premiumAmount
        self.coverageAmount = coverageAmount
        self.termYears = termYears

    def __str__(self):
        return (f"Policy [ID: {self.policyId}, Name: {self.policyName}, Premium: {self.premiumAmount}, "
                f"Coverage: {self.coverageAmount}, Term: {self.termYears} years]")
