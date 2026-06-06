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
    """Orchestrates the planner and researcher agents to build and verify a trip itinerary."""

    def kickoff(self, inputs: dict):
        """Run the crew with the given trip inputs and persist the result.

        Args:
            inputs: Dictionary with trip details such as destination, dates,
                    budget, travelers, and interests.

        Returns:
            A tuple of (crew_result, saved_file_path). The file path may be None
            if writing the plan to disk failed.
        """
        try:
            # Step 1: Ask the planner agent to create an initial day-by-day itinerary.
            plan_task = Task(
                description=f"Plan a trip to {inputs['destination']}",
                agent=planner,
                expected_output="A day-by-day itinerary in Markdown"
            )

            # Step 2: Ask the researcher agent to verify and refine the itinerary.
            research_task = Task(
                description="Verify and improve the plan",
                agent=researcher,
                expected_output="Verified itinerary with corrections"
            )

            # Build a sequential crew: planner runs first, then researcher reviews its output.
            crew = Crew(
                agents=[planner, researcher],
                tasks=[plan_task, research_task],
                process="sequential",
                max_iterations=6  # Guard against runaway agent loops.
            )

            # Execute the crew with the trip details available as context.
            result = crew.kickoff(inputs=inputs)

        except Exception as exc:
            # Wrap any crew failure in a domain-specific exception for the API layer.
            raise CrewExecutionError(f"Agent run failed: {exc}") from exc

        # === SAVE PLAN ===
        # Persist the generated itinerary alongside the original trip inputs for record keeping.
        os.makedirs("plans", exist_ok=True)
        filename = f"plans/plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump({"trip": inputs, "itinerary": str(result)}, f, indent=2, ensure_ascii=False)
            print(f"\n💾 Plan saved to: {filename}")
        except OSError as exc:
            # Non-fatal: log the error and continue returning the result to the caller.
            print(f"\n⚠️ Could not save plan to disk: {exc}")
            filename = None
        # =================

        return result, filename
