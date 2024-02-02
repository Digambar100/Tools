import requests
import sys

def request(url, file_handle):
    try:
        response = requests.get("https://" + url)
        if response.status_code == 200:
            print(f"[+] Subdomain discovered ----> {url}")
            file_handle.write(url + "\n")
    except requests.exceptions.RequestException as e:
        # Handle specific exceptions if needed
        pass

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <target_url> <output_file>")
        sys.exit(1)

    target_url = sys.argv[1]
    output_file = sys.argv[2]

    # Open subdomain list
    with open("bestdnswordlist.txt", "r") as wordlist, open(output_file, "a+") as file_handle:
        for line in wordlist:
            word = line.strip()
            test_url = f"{word}.{target_url}"
            request(test_url, file_handle)

if __name__ == "__main__":
    main()
