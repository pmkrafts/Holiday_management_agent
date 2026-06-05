from crewai import Crew, Task
from agents.planner import planner
from agents.researcher import researcher

class HolidayCrew:
    def kickoff(self, inputs: dict):
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
        
        return crew.kickoff(inputs=inputs)