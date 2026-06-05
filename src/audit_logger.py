"""
Audit and Traceability Controls
Author: Sasibhushan Rao Chanthati
"""

import json
from datetime import datetime


class AuditLogger:

    @staticmethod
    def log_event(
        event_type,
        user,
        action
    ):

        record = {
            "timestamp":
            datetime.utcnow().isoformat(),

            "event_type":
            event_type,

            "user":
            user,

            "action":
            action
        }

        print(
            json.dumps(
                record,
                indent=4
            )
        )


AuditLogger.log_event(
    "AI_REQUEST",
    "Analyst01",
    "Knowledge Retrieval"
)
