from prometheus_client import Counter

prediction_counter = Counter(
    'total_predictions',
    'Total Predictions'
)

api_counter = Counter(
    'total_calls',
    'Total Calls'
)

