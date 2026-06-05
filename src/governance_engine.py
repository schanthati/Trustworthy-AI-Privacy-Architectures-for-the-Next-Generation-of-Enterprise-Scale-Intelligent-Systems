"""
Governance-Aware Orchestration Framework
Author: Sasibhushan Rao Chanthati
"""


class GovernanceEngine:

    def evaluate_access(
        self,
        user_role,
        classification
    ):

        if user_role == "Administrator":
            return True

        if classification == "Restricted":
            return False

        return True

    def policy_decision(
        self,
        request
    ):

        approved = self.evaluate_access(
            request["role"],
            request["classification"]
        )

        return {
            "approved": approved,
            "policy":
            "Enterprise Trustworthy AI Governance Policy"
        }


engine = GovernanceEngine()

response = engine.policy_decision(
    {
        "role": "Analyst",
        "classification": "Internal"
    }
)

print(response)
