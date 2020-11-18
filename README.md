# Async-WebDir-Enum

Async WebDir Enum is a very simple Python script to bruteforce web directories using async requests.

## Installation

Use pip to install the requirements file.
```
pip install -r requirements.txt
```

## Arguments

|Flags|Args       |Description                                             |
|-----|-----------|--------------------------------------------------------|
|-u   |--url      |The url to enumerate                                    |
|-w   |--wordlist |The wordlist to use                                     |
|-s   |--semaphore|The number of concurrent REQUESTS (not threads) to allow|

## Misc

Like I said, this was just a simple project to learn how to use asyncio and aiohttp. If you would like to contribute with something, please, feel free to open an issue.
