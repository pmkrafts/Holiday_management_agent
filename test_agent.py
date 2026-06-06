from agents.crew import HolidayCrew

result, saved_path = HolidayCrew().kickoff({
    "destination": "Sikkim",
    "start_date": "2026-07-01",
    "end_date": "2026-07-05",
    "budget": 40000,
    "travelers": 2,
    "interests": "mountain, nightlife, trekking"
})
print("\n\n=== FINAL ITINERARY ===\n")
print(result)
if saved_path:
    print(f"\n💾 Saved to: {saved_path}")
