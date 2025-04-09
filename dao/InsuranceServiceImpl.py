from util.db_connection import get_connection
from util.dbproperty import get_connection_props
from exception.exceptions import PolicyNotFoundException

class InsuranceServiceImpl:
    def __init__(self):
        try:
            props = get_connection_props("util/db.properties")
            self.conn = get_connection(props)
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise Exception(f"Error initializing database connection: {e}")

    def createPolicy(self, policy):
        try:
            query = "INSERT INTO Policies (policyName, premiumAmount, coverageAmount, termYears) VALUES (%s, %s, %s, %s)"
            values = (policy.policyName, policy.premiumAmount, policy.coverageAmount, policy.termYears)
            self.cursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Error adding policy: {e}")

    def getPolicy(self, policyId):
        try:
            query = "SELECT * FROM Policies WHERE policyId = %s"
            self.cursor.execute(query, (policyId,))
            result = self.cursor.fetchone()
            if not result:
                raise PolicyNotFoundException(f"Policy with ID {policyId} not found.")
            return result
        except Exception as e:
            raise Exception(f"Error fetching policy: {e}")

    def getAllPolicies(self):
        try:
            query = "SELECT * FROM Policies"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            raise Exception(f"Error fetching all policies: {e}")

    def updatePolicy(self, policy):
        try:
            query = "UPDATE Policies SET policyName = %s, premiumAmount = %s, coverageAmount = %s, termYears = %s WHERE policyId = %s"
            values = (policy.policyName, policy.premiumAmount, policy.coverageAmount, policy.termYears, policy.policyId)
            self.cursor.execute(query, values)
            if self.cursor.rowcount == 0:
                raise PolicyNotFoundException(f"Policy with ID {policy.policyId} not found.")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Error updating policy: {e}")

    def deletePolicy(self, policyId):
        try:
            query = "DELETE FROM Policies WHERE policyId = %s"
            self.cursor.execute(query, (policyId,))
            if self.cursor.rowcount == 0:
                raise PolicyNotFoundException(f"Policy with ID {policyId} not found.")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Error deleting policy: {e}")

    def __del__(self):
        try:
            if hasattr(self, 'cursor') and self.cursor:
                self.cursor.close()
            if hasattr(self, 'conn') and self.conn:
                self.conn.close()
        except Exception as e:
            pass
