import requests

def sen_req(url):
    for i in range(1, 100000):
        try:
            requests.get(url)
            print(f"Request {i} sent successfully.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    target_url = "http://example.com"  # Replace with the desired URL
    sen_req(target_url) 