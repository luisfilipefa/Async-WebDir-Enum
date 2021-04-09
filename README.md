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

## Usage

``` 
python webdirenum.py -u http://example.com -w wordlist.txt -s 30
```
