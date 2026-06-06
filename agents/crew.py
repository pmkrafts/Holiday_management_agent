import json
import os
from datetime import datetime
from crewai import Crew, Task
from agents.planner import planner
from agents.researcher import researcher


class CrewExecutionError(Exception):
    """Raised when the CrewAI agents fail to execute or loop forever."""
    pass


class HolidayCrew:
    def kickoff(self, inputs: dict):
        try:
            plan_task = Task(
                description=f"Plan a trip to {inputs['destination']}",
                agent=planner,
                expected_output="A day-by-day itinerary in Markdown"
            )

            research_task = Task(
                description="Verify and improve the plan",
                agent=researcher,
                expected_output="Verified itinerary with corrections"
            )

            crew = Crew(
                agents=[planner, researcher],
                tasks=[plan_task, research_task],
                process="sequential",
                max_iterations=6
            )

            result = crew.kickoff(inputs=inputs)

        except Exception as exc:
            raise CrewExecutionError(f"Agent run failed: {exc}") from exc

        # === SAVE PLAN ===
        os.makedirs("plans", exist_ok=True)
        filename = f"plans/plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump({"trip": inputs, "itinerary": str(result)}, f, indent=2, ensure_ascii=False)
            print(f"\n💾 Plan saved to: {filename}")
        except OSError as exc:
            print(f"\n⚠️ Could not save plan to disk: {exc}")
            filename = None
        # =================

        return result, filename
