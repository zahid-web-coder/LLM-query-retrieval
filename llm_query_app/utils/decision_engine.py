def infer_decision(query: str, explanations: list) -> dict:
    decision = "Rejected"
    amount = "INR 0"
    reason = []

    query = query.lower()

    for explanation in explanations:
        explanation = explanation.lower()

        # Rule: Approval for coverage after 3 months / 90 days
        if "knee surgery" in query or "surgery" in query:
            if ("covered" in explanation and ("90 days" in explanation or "3 months" in explanation)):
                decision = "Approved"
                amount = "INR 5,00,000"
                reason.append(explanation)

        # Rule: Pre-existing conditions not covered
        if "pre-existing" in explanation and "not covered" in explanation:
            if "pre-existing" in query:
                decision = "Rejected"
                amount = "INR 0"
                reason.append(explanation)

        # Rule: Accident-related coverage
        if "accident" in query:
            if "accident" in explanation and ("covered" in explanation or "emergency hospitalization" in explanation):
                decision = "Approved"
                amount = "INR 2,00,000"
                reason.append(explanation)

        # Rule: Cosmetic not covered
        if "cosmetic" in query or "plastic surgery" in query:
            if "cosmetic" in explanation and "not covered" in explanation:
                decision = "Rejected"
                amount = "INR 0"
                reason.append(explanation)

    return {
        "decision": decision,
        "amount": amount,
        "justification": reason if reason else ["No direct matching clause found."]
    }
