from dao.InsuranceServiceImpl import InsuranceServiceImpl
from entity.Policy import Policy
from exception.exceptions import PolicyNotFoundException, InvalidInputException


def display_menu():
    print("\nInsurance Management System")
    print("1. Create Policy")
    print("2. View Policy")
    print("3. View All Policies")
    print("4. Update Policy")
    print("5. Delete Policy")
    print("6. Exit")


def main():
    service = InsuranceServiceImpl()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                policyName = input("Enter policy name: ")
                premiumAmount = float(input("Enter premium amount: "))
                coverageAmount = float(input("Enter coverage amount: "))
                termYears = int(input("Enter term (in years): "))
                policy = Policy(policyName=policyName, premiumAmount=premiumAmount, coverageAmount=coverageAmount, termYears=termYears)
                service.createPolicy(policy)
                print("Policy created successfully.")
            except ValueError:
                print("Error: Please enter valid numeric values for premium, coverage, and term.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                policyId = int(input("Enter policy ID: "))
                policy = service.getPolicy(policyId)
                print(f"Policy Details: {policy}")
            except PolicyNotFoundException as e:
                print(f"Error: {e}")
            except ValueError:
                print("Error: Please enter a valid numeric policy ID.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                policies = service.getAllPolicies()
                print("\nAll Policies:")
                for policy in policies:
                    print(f"ID: {policy[0]}, Name: {policy[1]}, Premium: {policy[2]}, Coverage: {policy[3]}, Term: {policy[4]} years")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                policyId = int(input("Enter policy ID to update: "))
                policyName = input("Enter new policy name: ")
                premiumAmount = float(input("Enter new premium amount: "))
                coverageAmount = float(input("Enter new coverage amount: "))
                termYears = int(input("Enter new term (in years): "))
                policy = Policy(policyId=policyId, policyName=policyName, premiumAmount=premiumAmount, coverageAmount=coverageAmount, termYears=termYears)
                service.updatePolicy(policy)
                print("Policy updated successfully.")
            except PolicyNotFoundException as e:
                print(f"Error: {e}")
            except ValueError:
                print("Error: Please enter valid numeric values for premium, coverage, and term.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                policyId = int(input("Enter policy ID to delete: "))
                service.deletePolicy(policyId)
                print("Policy deleted successfully.")
            except PolicyNotFoundException as e:
                print(f"Error: {e}")
            except ValueError:
                print("Error: Please enter a valid numeric policy ID.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
