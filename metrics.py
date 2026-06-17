from prometheus_client import Counter

prediction_counter = Counter(
    'total_prediction',
    'Total Predictions'
)

api_counter = Counter(
    'total_api_calls',
    'Total Api Calls'
)

