from agents.crew import HolidayCrew

result = HolidayCrew().kickoff({
    "destination": "Goa",
    "start_date": "2026-07-01",
    "end_date": "2026-07-05",
    "budget": 40000,
    "travelers": 2,
    "interests": "beach, nightlife"
})
print("\n\n=== FINAL ITINERARY ===\n")
print(result)
