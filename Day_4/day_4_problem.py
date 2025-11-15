data = """
Day 1:
- Sentiment API: 45 requests, 43 successful (200), 2 failed (500)
- Text Generation API: 28 requests, 28 successful (200), 0 failed
- Image Classification API: 67 requests, 65 successful (200), 2 failed (404)

Day 2:
- Sentiment API: 52 requests, 50 successful (200), 2 failed (401)
- Text Generation API: 31 requests, 29 successful (200), 2 failed (429)
- Image Classification API: 74 requests, 74 successful (200), 0 failed

Day 3:
- Sentiment API: 38 requests, 36 successful (200), 2 failed (500)
- Text Generation API: 42 requests, 42 successful (200), 0 failed
- Image Classification API: 81 requests, 78 successful (200), 3 failed (503)

Day 4:
- Sentiment API: 61 requests, 61 successful (200), 0 failed
- Text Generation API: 25 requests, 23 successful (200), 2 failed (400)
- Image Classification API: 53 requests, 51 successful (200), 2 failed (404)

Day 5:
- Sentiment API: 47 requests, 45 successful (200), 2 failed (429)
- Text Generation API: 39 requests, 39 successful (200), 0 failed
- Image Classification API: 92 requests, 90 successful (200), 2 failed (500)

Day 6:
- Sentiment API: 55 requests, 55 successful (200), 0 failed
- Text Generation API: 33 requests, 31 successful (200), 2 failed (503)
- Image Classification API: 68 requests, 66 successful (200), 2 failed (404)

Day 7:
- Sentiment API: 44 requests, 42 successful (200), 2 failed (401)
- Text Generation API: 37 requests, 37 successful (200), 0 failed
- Image Classification API: 75 requests, 73 successful (200), 2 failed (500)
"""
import re


def parse_data(data):
    api_data = dict()
    processed_data = re.split(r"\n Day /d+:\n", data)
    for index, value in enumerate(processed_data):
        day = f"\n Day {index + 1}:\n"
        pattern = re.findall(
            r"- (.*?): (\d+) requests, (\d+) successful \(200\), (\d+) failed \((\d+)\)",
            value,
        )
        for api, requests, successful, failed, error_code in pattern:
            if day not in api_data:
                api_data[day] = []
            api_data[day].append(
                {
                    "api": api,
                    "requests": int(requests),
                    "successful": int(successful),
                    "failed": int(failed),
                    "error_code": int(error_code),
                }
            )
    return api_data


def check_total_request_for_each_api(api_data):
    total_requests = {}
    for day, apis in api_data.items():
        for api_info in apis:
            api_name = api_info["api"]
            requests = api_info["requests"]
            if api_name not in total_requests:
                total_requests[api_name] = 0
            total_requests[api_name] += requests
    return total_requests


if __name__ == "__main__":
    parsed_data = parse_data(data)
    print(check_total_request_for_each_api(parsed_data))
