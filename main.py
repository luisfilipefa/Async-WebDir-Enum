import asyncio, aiohttp, pathlib, argparse, time
from datetime import datetime
from fake_headers import Headers

def args_parser():
    parser = argparse.ArgumentParser(prog="Python script to bruteforce web directories using asyncio")
    parser.add_argument("-u", "--url", help="The url to brute force (Include HTTP schema)", type=str, required=True)
    parser.add_argument("-w", "--wordlist", help="The wordlist to use", type=str, required=True)
    parser.add_argument("-s", "--semaphore", help="The number of simultaneous requests to the url (Default 50)", type=int, required=False, default=50)
    args = parser.parse_args()
    return args

async def check_url_status(url, session):
    try:
        async with session.get(url, headers=Headers(headers=False).generate()) as response:
            status_code = response.status
            if status_code == 200:
                print(f"[*] Found: {url.strip()} (Status {status_code})")
                return 1
    except aiohttp.ClientError:
        print("[!] Connection error...")

async def main():
    start = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    ts = time.perf_counter()

    args = args_parser()
    wordlist = pathlib.Path(args.wordlist).resolve()
    urls = (f"{args.url}/{url}" for url in wordlist.open(mode="r") if not url.startswith("#"))

    print("-"*50)
    print(f"[*] Started at {start} [*]")
    print("-"*50)
    print(f"[*] Host: {args.url}")
    print(f"[*] Wordlist: {args.wordlist}")
    print("-"*50)

    async with asyncio.Semaphore(args.semaphore):
        async with aiohttp.ClientSession() as session:
            tasks = (check_url_status(url, session) for url in urls)

            urls_found = await asyncio.gather(*tasks)

            total_urls_found = 0

            for url_found in urls_found:
                if not url_found is None:
                    total_urls_found+=url_found

            print("-"*50)
            print(f"[*] Found {total_urls_found} urls [*]")

    te = time.perf_counter()
    end = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    
    print("-"*50)
    print(f"[*] Finished at {end} | {round(te-ts, 2)} seconds [*]")
    print("-"*50)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass