from prometheus_client import Counter

prediction_counter = Counter(
    "total_predictions",
    "Total predictions made"
)

api_requests = Counter(
    "total_api_requests",
    "Total API requests"
)