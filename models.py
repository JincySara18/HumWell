# check_models.py
import google.generativeai as palm
import traceback

palm.configure(api_key="AIzaSyDeFj6s8wcOP_LwXzuKJAtB55kSb9PjxQw")

try:
    print("✅ Listing models:")
    for m in palm.list_models():
        print(f"{m.name} → {m.supported_generation_methods}")
except Exception:
    print(" Error while listing models:")
    traceback.print_exc()
